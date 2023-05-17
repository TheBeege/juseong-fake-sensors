import uuid

from pydantic import BaseModel


class MetricModel(BaseModel):
    unit: str
    measure: float
    timestamp: int


class SensorModel(BaseModel):
    id: uuid.UUID
    type: str
