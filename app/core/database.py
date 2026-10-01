import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings

def get_normalized_database_url(raw_url: str) -> str:
    url = raw_url.strip()
    if url.startswith("postgres://"):
        url = "postgresql+asyncpg://" + url[len("postgres://"):]
    elif url.startswith("postgresql://") and not url.startswith("postgresql+asyncpg://"):
        url = "postgresql+asyncpg://" + url[len("postgresql://"):]
    return url

db_url = get_normalized_database_url(settings.DATABASE_URL)

if db_url.startswith("sqlite"):
    os.makedirs("data", exist_ok=True)
    engine = create_async_engine(
        db_url,
        echo=False,
        future=True
    )
else:
    engine = create_async_engine(
        db_url,
        echo=False,
        future=True,
        pool_pre_ping=True,
        pool_recycle=300,
        connect_args={"prepared_statement_cache_size": 0}
    )

async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
