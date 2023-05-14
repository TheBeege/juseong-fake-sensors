FROM python:3.11

LABEL org.opencontainers.image.source="https://github.com/TheBeege/juseong-fake-sensors"

WORKDIR /usr/src/app

COPY . .

# TODO: figure out how to install dependencies without actual application
RUN python -m pip install --no-cache --upgrade pip && \
    python -m pip install --no-cache .

CMD ["fake_sensors"]
