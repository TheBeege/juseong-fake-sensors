# Fake Sensors for Juseong

Just some fake sensor systems for Juseong to practice building data systems from

## Setup
For local dev:

```shell
python -m venv venv
python -m pip install --upgrade pip
python -m pip install -e .
```

## Running
After setup:

```shell
COLLECTION_MODE=http fake_sensors
```

Then open up your browser to the [Swagger docs page](http://127.0.0.1:8000/docs)

MQTT mode is pending. HTTP mode is lacking the actual fake data yet.

## Docker
```shell
docker build . -t thebeege/juseong-fake-sensors:latest
```
