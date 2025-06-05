from fastapi import FastAPI
from routing.routs import router as products_routing

app = FastAPI(openapi_url="/openapi.json", docs_url="/docs", debug=True)

app.include_router(products_routing)
