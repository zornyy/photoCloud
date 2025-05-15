from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from typing import Generator, AsyncGenerator
from core.config import settings  # Use the settings object directly

# Create connection URLs for both sync and async
DATABASE_URL = settings.DATABASE_URL
ASYNC_DATABASE_URL = DATABASE_URL.replace("mysql+pymysql", "mysql+aiomysql")

# Create synchronous engine and session
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False
)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# Create async engine and session
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=3600
)
AsyncSessionLocal = sessionmaker(
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
    bind=async_engine
)

# Create a base class for SQLAlchemy models
Base = declarative_base()

# Dependency for synchronous routes
def get_db() -> Generator:
    """
    Dependency function to get a database session for synchronous routes
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency for asynchronous routes
async def get_async_db() -> AsyncGenerator:
    """
    Dependency function to get a database session for asynchronous routes
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()