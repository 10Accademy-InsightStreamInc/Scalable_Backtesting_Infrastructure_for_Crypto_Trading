from sqlalchemy import Boolean, Column, Integer, Float, Date, ForeignKey, TIMESTAMP, String, Text, text
from sqlalchemy.orm import relationship
from .database import Base

class Indicator(Base):
    __tablename__ = 'indicators'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    symbol = Column(String, nullable=False, unique=True)
    description = Column(Text)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    
class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    symbol = Column(String, nullable=False, unique=True)
    description = Column(Text)

class Scene(Base):
    __tablename__ = 'scenes'
    id = Column(Integer, primary_key=True, index=True)
    period = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    stock_name = Column(String, ForeignKey('stocks.name'))
    indicator_id = Column(Integer, ForeignKey('indicators.id'))
    backtests = relationship('BacktestResult', back_populates='scene')
    indicator = relationship('Indicator')

class BacktestResult(Base):
    __tablename__ = 'backtest_results'
    id = Column(Integer, primary_key=True, index=True)
    scene_id = Column(Integer, ForeignKey('scenes.id'))
    gross_profit = Column(Float, nullable=False)
    net_profit = Column(Float, nullable=False)
    number_of_trades = Column(Integer, nullable=False)
    winning_trades = Column(Integer)
    losing_trades = Column(Integer)
    max_drawdown = Column(Float)
    sharpe_ratio = Column(Float)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    scene = relationship('Scene', back_populates='backtests')
