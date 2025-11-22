"""
Database configuration and session management.
Implements the Dependency Injection pattern for database sessions.
"""

from collections.abc import AsyncGenerator, Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""


# Parse base database URL
base_db_url = make_url(str(settings.database.database_url))

# Synchronous engine for Alembic migrations
sync_db_url = base_db_url.set(drivername="postgresql+psycopg2")
sync_engine = create_engine(
    sync_db_url,
    pool_size=settings.database.database_pool_size,
    max_overflow=settings.database.database_max_overflow,
    echo=settings.database.database_echo,
    pool_pre_ping=True,
)

# Asynchronous engine for FastAPI
async_db_url = base_db_url.set(drivername="postgresql+asyncpg")
async_engine = create_async_engine(
    async_db_url,
    pool_size=settings.database.database_pool_size,
    max_overflow=settings.database.database_max_overflow,
    echo=settings.database.database_echo,
    pool_pre_ping=True,
)

# Session factories
SyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=sync_engine,
    class_=Session,
)

AsyncSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


def get_sync_db() -> Generator[Session, None, None]:
    """
    Dependency for synchronous database session.
    Follows the Dependency Injection pattern.
    """
    db = SyncSessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency for asynchronous database session.
    Follows the Dependency Injection pattern.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


async def init_db() -> None:
    """Initialize database tables."""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_db() -> None:
    """Close database connections."""
    await async_engine.dispose()
