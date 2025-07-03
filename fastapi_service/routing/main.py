import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI

from application.services.product_redis_kafka_service import consume, consumer
from routing.routs import router as products_routing


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(consume())
    yield
    await consumer.stop()


app = FastAPI(
    openapi_url='/openapi.json',
    docs_url='/docs',
    lifespan=lifespan,
    debug=True)

app.include_router(products_routing)
