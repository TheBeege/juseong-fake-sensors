from datetime import datetime

from fake_sensors.sensor.base import BaseSensor, BaseUnit, Metric


class TemperatureUnit(BaseUnit):
    DEGREES_CELSIUS = "degrees_celsius"
    DEGREES_FAHRENHEIT = "degrees_fahrenheit"


class TemperatureSensor(BaseSensor):
    def __init__(
        self,
        minimum: float,
        maximum: float,
        distribution: float,
        units: TemperatureUnit = TemperatureUnit.DEGREES_CELSIUS,
    ):
        super().__init__(minimum, maximum, distribution)
        self.units: TemperatureUnit = units

    def get_metric(self):
        measure_value = self.generate_value() * 100
        return Metric(
            unit=self.units,
            measure=measure_value,
            timestamp=datetime.utcnow(),
        )
