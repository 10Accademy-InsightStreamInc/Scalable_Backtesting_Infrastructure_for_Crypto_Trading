from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
import pandas as pd
import json
import os, sys

cwd=os.getcwd()
sys.path.append(f"{cwd}/backend/utils/")
sys.path.append(f"{cwd}/scripts/")

print("The os is :: ", os.getcwd())

from backend.utils.backtest import run_backtest

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/health')
def check_health():
    return "API is healthy"

@app.post('/indicators/', response_model=schemas.Indicator)
def create_indicator(indicator: schemas.IndicatorCreate, db: Session = Depends(get_db)):
    db_indicator = models.Indicator(**indicator.model_dump())
    db.add(db_indicator)
    db.commit()
    db.refresh(db_indicator)
    return db_indicator

@app.get('/indicators/', response_model=List[schemas.Indicator])
def read_indicators(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    indicators = db.query(models.Indicator).offset(skip).limit(limit).all()
    return indicators

@app.post('/stocks/', response_model=schemas.Stock)
def create_stock(stock: schemas.StockCreate, db: Session = Depends(get_db)):
    db_stock = models.Stock(**stock.model_dump())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

@app.get('/stocks/', response_model=List[schemas.Stock])
def read_stocks(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    stocks = db.query(models.Stock).offset(skip).limit(limit).all()
    return stocks

@app.post('/scenes/', response_model=schemas.Scene)
def create_scene(scene: schemas.SceneCreate, db: Session = Depends(get_db)):
    db_scene = models.Scene(**scene.model_dump())
    db.add(db_scene)
    db.commit()
    db.refresh(db_scene)
    return db_scene

@app.get('/scenes/', response_model=List[schemas.Scene])
def read_scenes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    scenes = db.query(models.Scene).offset(skip).limit(limit).all()
    return scenes

@app.post('/backtests/{scene_id}', response_model=List[schemas.BacktestResult])
def perform_backtest(scene_id: int, db: Session = Depends(get_db)):
    db_scene = db.query(models.Scene).filter(models.Scene.id == scene_id).first()
    if db_scene is None:
        raise HTTPException(status_code=404, detail="Scene not found")

    # Fetch data based on the scene's date range
    df = fetch_data(db_scene.start_date, db_scene.end_date)
    
    # Perform backtest
    metrics = run_backtest({
        'period': db_scene.period,
        'indicator_name': db_scene.indicator.name
    }, df)

    # Save metrics to database
    backtest_results = []
    for metric in metrics:
        db_backtest_result = models.BacktestResult(scene_id=scene_id, **metric)
        db.add(db_backtest_result)
        db.commit()
        db.refresh(db_backtest_result)
        backtest_results.append(db_backtest_result)

    return backtest_results

@app.get('/run_backtest/', response_model=List[schemas.BacktestResult])
def run_backtests(scene: schemas.SceneCreate, db: Session = Depends(get_db)):
    db_scene = models.Scene(**scene.model_dump())
    return db_scene

@app.get('/backtest_results/', response_model=List[schemas.BacktestResult])
def read_backtest_results(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    backtest_results = db.query(models.BacktestResult).offset(skip).limit(limit).all()
    return backtest_results

def fetch_data(start_date, end_date):
    # Replace this with actual data fetching logic
    df = pd.read_csv('btc_usdt_candlestick.csv', index_col='timestamp', parse_dates=True)
    return df.loc[start_date:end_date]
