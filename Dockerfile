ARG BASE_IMAGE=python:3.10-slim

FROM ${BASE_IMAGE} as base

LABEL maintainer='abc'

RUN apt-get update && apt-get install -y make && apt-get clean

# Use the opt directory as our dev directory
WORKDIR /opt

ENV PYTHONUNBUFFERED=TRUE \
    PYTHONPATH="${PYTHONPATH}:/opt"

COPY requirements.dev .
COPY requirements.prod .

# Install python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir wheel \
    && pip install --no-cache-dir -r requirements.dev \
    && pip install --no-cache-dir -r requirements.prod \
    && pip list
