from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv('DATABASE_URL', "postgresql+psycopg2://group_three:lbRFEbA2bf3g5x6iDRrIsNqLycCznpab@dpg-cp6uiansc6pc73cnh6f0-a.oregon-postgres.render.com/amharic_contents")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()