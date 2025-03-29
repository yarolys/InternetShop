FROM python:3.12.8-alpine
WORKDIR /backend
RUN apk upgrade --update && apk add gcc gcompat musl-dev libffi-dev build-base unixodbc-dev unixodbc --no-cache
COPY pyproject.toml uv.lock ./
RUN pip install uv
RUN uv pip install --system .
COPY alembic.ini README.md ./
COPY app.py .
COPY src/ ./src