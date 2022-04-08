FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  && apt-get install -y curl \
  && apt-get dist-upgrade -y \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN python -m pip install --upgrade pip \
  && python -m pip install --upgrade setuptools \
  && python -m pip install poetry==1.1.13

# Requirements are installed here to ensure they will be cached.
COPY ./backend/poetry.lock /poetry.lock
COPY ./backend/pyproject.toml /pyproject.toml
RUN poetry config virtualenvs.create false && poetry install

WORKDIR /app
