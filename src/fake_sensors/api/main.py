import os

import uvicorn
from fastapi import FastAPI

from fake_sensors.api.routes import router


def run():
    try:
        port = int(os.getenv("PORT", 8000))
    except TypeError:
        raise OSError("The PORT environment variable must be a valid integer")
    log_level = os.getenv("LOG_LEVEL", "info")

    app = FastAPI()
    app.include_router(router)

    uvicorn.run(app, host="0.0.0.0", port=port, log_level=log_level)
