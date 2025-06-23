from typing import Callable, Generator

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from adapters.database.database import async_engine
from adapters.database.tables.models_db import mapper_registry


@pytest_asyncio.fixture
async def async_session() -> AsyncSession:
    session = sessionmaker(
        async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with session() as s:
        async with async_engine.begin() as conn:
            await conn.run_sync(mapper_registry.metadata.create_all)

        yield s

    async with async_engine.begin() as conn:
        await conn.run_sync(mapper_registry.metadata.drop_all)

    await async_engine.dispose()

    @pytest_asyncio.fixture
    async def http_client(
            async_session: AsyncSession,
    ) -> Generator[AsyncClient, None, None]:
        async with (
            AsyncClient(base_url="http://0.0.0.0:9000") as ac,
        ):
            yield ac
