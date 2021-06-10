# syntax=docker/dockerfile:1
FROM tensorflow/tensorflow
COPY . /scripts
CMD python /scripts/main.py
