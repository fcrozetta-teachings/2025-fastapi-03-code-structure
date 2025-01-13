import time
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

from middlewares.performance_monitor import performance_header

from routers.user_router import app as user_router
from routers.products_router import app as products_router
from routers.user_addresses_router import app as user_adresses_router


app = FastAPI(title="Fcrozetta API - Parameters")
app.add_middleware(BaseHTTPMiddleware, dispatch=performance_header)
app.include_router(user_router)
app.include_router(products_router)
app.include_router(user_adresses_router)
