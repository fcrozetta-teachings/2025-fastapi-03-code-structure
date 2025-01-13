import time
from fastapi import FastAPI, Request
from routers.user_router import app as user_router
from routers.products_router import app as products_router
from routers.user_addresses_router import app as user_adresses_router


app = FastAPI(title="Fcrozetta API - Parameters")
app.include_router(user_router)
app.include_router(products_router)
app.include_router(user_adresses_router)


@app.middleware("http")
async def performance_header(request: Request, call_next):
    # Start the perf counter
    start_time = time.perf_counter()

    # Call the api/next middleware, etc
    response = await call_next(request)

    # Calculate the time taken
    process_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = str(process_time)

    return response
