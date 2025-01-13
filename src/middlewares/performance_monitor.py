import time
from fastapi import Request


async def performance_header(request: Request, call_next):
    # Start the perf counter
    start_time = time.perf_counter()

    # Call the api/next middleware, etc
    response = await call_next(request)

    # Calculate the time taken
    process_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = str(process_time)

    return response
