from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv('DATABASE_URL', "postgresql://trading_db_av2v_user:210M6MA9QKEEgVdiasnUdMQDBNN417oy@dpg-cpqojbqj1k6c73bkqq3g-a.oregon-postgres.render.com/trading_db_av2v")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()