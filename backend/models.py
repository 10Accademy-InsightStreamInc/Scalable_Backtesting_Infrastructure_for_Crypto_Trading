from sqlalchemy import Boolean, Column, Integer, Float, Date, ForeignKey, TIMESTAMP, String, Text, text, UniqueConstraint
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
    stock_id = Column(Integer, ForeignKey('stocks.id'))
    indicator_id = Column(Integer, ForeignKey('indicators.id'))
    backtests = relationship('BacktestResult', back_populates='scene')
    stock = relationship('Stock')
    indicator = relationship('Indicator')

    __table_args__ = (UniqueConstraint('start_date', 'end_date', 'indicator_id', 'stock_id', name='_scene_uc'),)

class BacktestResult(Base):
    __tablename__ = 'backtest_results'
    # __table_args__ = (UniqueConstraint('scene_id', 'indicator_id', 'stock_id', name='_backtest_uc'),)
    id = Column(Integer, primary_key=True, index=True)
    scene_id = Column(Integer, ForeignKey('scenes.id'))
    initial_cash = Column(Float, nullable=False)
    final_value = Column(Float, nullable=False)
    percentage_return = Column(Float)
    max_drawdown = Column(Float)
    total_trades = Column(Integer)
    winning_trades = Column(Integer)
    losing_trades = Column(Integer)
    sharpe_ratio = Column(Float)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    scene = relationship('Scene', back_populates='backtests')
