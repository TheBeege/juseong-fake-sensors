#!/usr/bin/env python
import os

from fake_sensors.api import run as api_run
from fake_sensors.mqtt import run as mqtt_run


def main():
    collection_mode = os.getenv("COLLECTION_MODE")
    if collection_mode == "http":
        api_run()
    elif collection_mode == "mqtt":
        mqtt_run()
    else:
        raise EnvironmentError("The COLLECTION_MODE environment variable must be set as 'http' or 'mqtt'")
