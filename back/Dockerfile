# Use an official Python image as the base
FROM python:3.12-slim

# Set environment variables with default values
ARG FRONTEND_URL=http://localhost:4200
ARG SELF_URL=http://localhost
ARG SELF_PORT=8000
ARG VERSION=0.0.1
ARG API_VERSION=1
ARG SEARCH_API_URL=http://localhost:52584
ENV FRONTEND_URL=${FRONTEND_URL}
ENV SELF_URL=${SELF_URL}
ENV SELF_PORT=${SELF_PORT}
ENV VERSION=${VERSION}
ENV API_VERSION=${API_VERSION}
ENV SEARCH_API_URL=${SEARCH_API_URL}

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy project files
COPY pyproject.toml poetry.lock ./
COPY . /app

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install

# Expose the application port
EXPOSE ${SELF_PORT}

# Command to run the application
CMD ["sh", "-c", "poetry run uvicorn main:app --host 0.0.0.0 --port ${SELF_PORT}"]
