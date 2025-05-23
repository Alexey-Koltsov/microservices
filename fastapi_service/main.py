from fastapi import FastAPI
from routing.items import router as items_routing

app = FastAPI(openapi_url="/openapi.json", docs_url="/docs")

app.include_router(items_routing)
