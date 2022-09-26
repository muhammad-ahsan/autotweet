# autotweet

1. A dockerized REST API that encapsulates a machine learning-based tweet model
2. A machine learning model based on the Markov chain.
3. Serve as a standalone tweet generative model
4. Given a request, the model provides a tweet. Can be parameterized in future


# Build Docker
docker build -t autotweet .

# Run Docker
docker run -p 8000:8000 autotweet

# API Interface
1. http://0.0.0.0:8000
2. http://0.0.0.0:8000/tweet
3. http://0.0.0.0:8000/health
4. http://0.0.0.0:8000/docs