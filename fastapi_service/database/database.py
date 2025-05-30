from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

POSTGRES_URL = "postgresql+asyncpg://admin:password@localhost:5432/db"

async_engine = create_async_engine(url=POSTGRES_URL, echo=True)

async_session = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
        await session.close()


# session - создание сессии для работы с БД
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    return get_async_session()
