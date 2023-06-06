# Fake Sensors for Juseong

Just some fake sensor systems for Juseong to practice building data systems from

## Usage

First, make sure you have [Docker installed](https://docs.docker.com/desktop/) or
[Rancher](https://rancherdesktop.io/) with the Docker CLI.

To run:

```shell
docker run --pull=always -p 8000:8000 ghcr.io/thebeege/juseong-fake-sensors:latest
```

Then open up your browser to the [Swagger docs page](http://127.0.0.1:8000/docs)

## Development

### Setup

For local dev:

```shell
python -m venv venv
python -m pip install --upgrade pip
python -m pip install -e .[dev]
pre-commit install
```

### Running

After setup:

```shell
COLLECTION_MODE=http fake_sensors
```

Then open up your browser to the [Swagger docs page](http://127.0.0.1:8000/docs)

MQTT mode is pending. HTTP mode is lacking the actual fake data yet.

### Docker

To build:

```shell
docker build . -t thebeege/juseong-fake-sensors:latest
```
