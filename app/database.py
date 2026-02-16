from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./librarysystem.db"

engine = create_engine(   #door to database
    DATABASE_URL,
    connect_args={"check_same_thread": False} #SQLite uses one thread,FastAPI uses multiple threads,so disable that
)

SessionLocal = sessionmaker(  #Each API request will use 1 session
    autocommit=False,         #Session is temp connection used to read/write data
    autoflush=False,
    bind=engine
)

Base = declarative_base() #Parent class for database tables

def get_db():             #This is a dependency that opens.gives access and closes DB automatically
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
