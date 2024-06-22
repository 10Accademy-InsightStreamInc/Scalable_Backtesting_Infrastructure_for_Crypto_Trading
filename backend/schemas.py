from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date, datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
    
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
