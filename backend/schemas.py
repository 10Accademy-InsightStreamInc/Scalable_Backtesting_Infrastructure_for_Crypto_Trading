from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date, datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str 
    
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str
    
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
    stock_id: int

class SceneCreate(SceneBase):
    pass

class Scene(SceneBase):
    id: int
    backtests: List['BacktestResult'] = []
    indicator: Indicator
    stock: Stock

    class Config:
        orm_mode = True

class BacktestResultBase(BaseModel):
    scene_id: int
    initial_cash: float
    final_value: float
    percentage_return: float
    total_trades: int
    winning_trades: int
    losing_trades: int
    sharpe_ratio: Optional[float] = None
    max_drawdown: Optional[float] = None

class BacktestResultCreate(BacktestResultBase):
    pass

class BacktestResult(BacktestResultBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class StockData(BaseModel):
    date: datetime
    symbol: str
    open: float
    high: float
    low: float
    close: float
    adj_close: float
    volume: float

    class Config:
        orm_mode = True