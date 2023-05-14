FROM python:3.11

LABEL org.opencontainers.image.source="https://github.com/TheBeege/juseong-fake-sensors"

WORKDIR /usr/src/app

EXPOSE 8000/tcp

ENV PORT=8000
ENV COLLECTION_MODE=http

COPY . .

# TODO: figure out how to install dependencies without actual application
RUN python -m pip install --no-cache-dir --upgrade pip~=23.1.2 && \
    python -m pip install --no-cache-dir .

CMD ["fake_sensors"]
