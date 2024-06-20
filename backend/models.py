from sqlalchemy import Column, Integer, Float, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Scene(Base):
    __tablename__ = 'scenes'
    id = Column(Integer, primary_key=True, index=True)
    period = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    backtests = relationship('BacktestResult', back_populates='scene')

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
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    scene = relationship('Scene', back_populates='backtests')
