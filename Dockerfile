FROM python:3.11-slim

WORKDIR /app

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        && rm -rf /var/lib/apt/lists/*

# Install Poetry and clean cache
RUN pip install --no-cache-dir "poetry>=2.2,<2.3"


COPY pyproject.toml poetry.lock* README.md /app/

# Install dependencies (no dev, no venv)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev --no-root

# Copy project code and models
COPY src/ src/
COPY models/ models/

# Expose FastAPI port
EXPOSE 8000

# Run uvicorn via Poetry
CMD ["poetry", "run", "uvicorn", "autotweet.app:app", "--host", "0.0.0.0", "--port", "8000"]
