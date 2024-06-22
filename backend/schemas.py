from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime

class IndicatorBase(BaseModel):
    name: str
    symbol: str
    description: Optional[str] = None

class IndicatorCreate(IndicatorBase):
    pass

class Indicator(IndicatorBase):
    id: int

    class Config:
        orm_mode = True

class StockBase(BaseModel):
    name: Optional[str] = None
    symbol: str
    description: Optional[str] = None

class StockCreate(StockBase):
    pass

class Stock(StockBase):
    id: int

    class Config:
        orm_mode = True

class SceneBase(BaseModel):
    period: int
    start_date: date
    end_date: date
    indicator_id: int

class SceneCreate(SceneBase):
    pass

class Scene(SceneBase):
    id: int
    backtests: List['BacktestResult'] = []
    indicator: Indicator

    class Config:
        orm_mode = True

class BacktestResultBase(BaseModel):
    scene_id: int
    gross_profit: float
    net_profit: float
    number_of_trades: int
    winning_trades: Optional[int] = None
    losing_trades: Optional[int] = None
    max_drawdown: Optional[float] = None
    sharpe_ratio: Optional[float] = None

class BacktestResultCreate(BacktestResultBase):
    pass

class BacktestResult(BacktestResultBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
