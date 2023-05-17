import uuid
from enum import Enum
from typing import Dict, List, Optional

from fake_sensors.sensor.base import BaseSensor
from fake_sensors.sensor.temperature import TemperatureSensor


class SensorType(str, Enum):
    TEMPERATURE = "temperature"


class SensorManager:
    def __init__(self):
        self._sensors_by_type: dict[SensorType, list[BaseSensor]] = {
            SensorType.TEMPERATURE: [
                TemperatureSensor(0, 150, 0),
                TemperatureSensor(0, 150, 0),
                TemperatureSensor(0, 150, 0),
            ],
        }
        self._sensors_by_id: dict[uuid.UUID, BaseSensor] = {}
        for sensor_list in self._sensors_by_type.values():
            for sensor in sensor_list:
                self._sensors_by_id[sensor.id] = sensor

    def get_sensors(
        self, type_name: SensorType | None = None
    ) -> list[BaseSensor]:
        if type_name is None:
            output_sensor_list = list()
            for sensor_list in self._sensors_by_type.values():
                output_sensor_list.extend(sensor_list)
            return output_sensor_list

        return self._sensors_by_type.get(type_name, [])

    def get_one_sensor(self, sensor_id: uuid.UUID) -> BaseSensor:
        return self._sensors_by_id.get(sensor_id, None)


sensor_manager = SensorManager()
