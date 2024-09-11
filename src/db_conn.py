from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from dotenv import load_dotenv
import os

load_dotenv()

uri = URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('PORT'),
    database=os.getenv('DATABASE')
)

print(uri)

# uri = "sqlite:///database.db"

engine = create_engine(uri)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
