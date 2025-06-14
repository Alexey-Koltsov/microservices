import asyncio

from fastapi import FastAPI

from application.services.product_redis_kafka_service import consume, consumer
from routing.routs import router as products_routing

app = FastAPI(openapi_url='/openapi.json', docs_url='/docs', debug=True)

app.include_router(products_routing)


@app.on_event('startup')
async def startup_event():
    asyncio.create_task(consume())


@app.on_event('shutdown')
async def shutdown_event():
    await consumer.stop()
