from sqlalchemy import create_engine
from sqlalchemy.orm import Sessionmaker, declarative_base
from urllib.parse import quote_plus

DB_USER = "root"
DB_PASS = quote_plus("pass")
DB_HOST = "localhost"
DB_NAME = "AXIS"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

