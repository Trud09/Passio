# syntax=docker/dockerfile:1
FROM tensorflow/tensorflow
COPY main.py /app/
RUN mkdir -p /model/
ENTRYPOINT python /app/main.py

