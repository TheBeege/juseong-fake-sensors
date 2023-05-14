from typing import Union

from fastapi import APIRouter

router = APIRouter()


@router.get("/sensors")
def list_sensors():
    return {"Hello": "World"}


@router.get("/sensors/{sensor_id}")
def read_sensor(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
