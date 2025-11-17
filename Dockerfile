# Use official Python base
FROM python:3.11-slim

# Install Poetry
RUN pip install --no-cache-dir poetry==2.2.1

# Set workdir
WORKDIR /app

# Copy project files
COPY pyproject.toml README.md ./
COPY src/ src/
COPY models/ models/

# Install dependencies (no dev deps, no venv creation)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev

# Expose FastAPI port
EXPOSE 8000

# Run uvicorn via Poetry
CMD ["poetry", "run", "uvicorn", "autotweet.app:app", "--host", "0.0.0.0", "--port", "8000"]