import uuid
from typing import List

from fastapi import APIRouter

from fake_sensors.api.schema import MetricModel, SensorModel
from fake_sensors.sensor.manager import SensorType, sensor_manager

router = APIRouter()


@router.get("/sensors")
def list_sensors(type_name: SensorType = None) -> list[SensorModel]:
    output_list = []
    # Yes, I don't like complex list comprehensions
    for sensor in sensor_manager.get_sensors(type_name):
        output_list.append(SensorModel(**sensor.to_dict()))
    return output_list


@router.get("/sensors/{sensor_id}")
def read_sensor(sensor_id: uuid.UUID) -> SensorModel:
    return SensorModel(**sensor_manager.get_one_sensor(sensor_id).to_dict())


@router.get("/sensors/{sensor_id}/metric")
def read_sensor(sensor_id: uuid.UUID) -> MetricModel:
    return MetricModel(
        **sensor_manager.get_one_sensor(sensor_id).get_metric().to_dict()
    )
