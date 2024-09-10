from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URL = URL.create(
    "postgresql+psycopg2",
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    database=os.getenv('DATABASE')
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()