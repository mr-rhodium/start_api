import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

pg_user = os.getenv("DATABASE_URL")
pg_password = os.getenv("DATABASE_PASSWORD")
pg_database = os.getenv("DATABASE_NAME")

database_url = f"postgresql://{pg_user}:{pg_password}@db:5432/{pg_database}"
engine = create_engine(database_url)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
