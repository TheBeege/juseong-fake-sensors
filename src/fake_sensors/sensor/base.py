import json
import random
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Dict, Union


class BaseUnit(str, Enum):
    """
    A base class for other units to inherit. Just sets the constraint that units are string enums
    """

    pass


class MetricMeasureType(str, Enum):
    """
    Defines how the measure value of a metric will be provided.
    Measures of the "sample" type provide a sample at a discrete points in time.
    Measures of the "cumulative" type continuously add to their value, essentially a counter.
    """

    SAMPLE = "sample"
    CUMULATIVE = "cumulative"


class Metric:
    """
    Describes a metric value obtained from a sensor, called a measure.
    A metric also provides the units of the measurement and an epoch timestamp of when the metric was generated.
    """

    def __init__(self, unit: BaseUnit, measure: float, timestamp: datetime):
        self._unit: BaseUnit = unit
        self._measure: float = measure
        self._timestamp: datetime = timestamp

    @property
    def unit(self):
        return self._unit

    @property
    def measure(self):
        return self._measure

    @property
    def timestamp(self):
        return self._timestamp.timestamp()

    def to_dict(self) -> dict[str, int | float | str]:
        return {
            "timestamp": self._timestamp.timestamp(),
            "unit": self._unit.name,
            "measure": self._measure,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


class BaseSensor(ABC):
    """
    A base class for other sensors. Allows configuration of how to generate metric values
    via minimum, maximum, and distribution parameters in its constructor. Allows metric collection
    by calling the `get_value` function.

    TODO: distribution
    """

    def __init__(self, minimum: float, maximum: float, distribution: float):
        self._id = uuid.uuid1()
        self.minimum = minimum
        self.maximum = maximum
        self.distribution = distribution

    @property
    def id(self):
        return self._id

    def generate_value(self) -> float:
        # TODO: use distribution
        return random.random()

    @abstractmethod
    def get_metric(self) -> Metric:
        pass

    def to_dict(self) -> dict[str, str]:
        return {"id": self._id, "type": self.__class__.__name__}

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
