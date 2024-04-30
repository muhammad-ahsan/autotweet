FROM python:3.11-slim

RUN pip install --upgrade pip setuptools
RUN pip install pipenv
RUN apt-get -q update && apt-get install -y --no-install-recommends gcc supervisor && rm -rf /var/lib/apt/lists/*

WORKDIR autotweet

COPY main.py .
COPY src ./src
COPY models/markov-chain ./models/markov-chain
COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy --ignore-pipfile --verbose

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["python", "main.py"]