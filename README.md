# autotweet


1. A dockerized REST API which encapsulates a machine learning based tweet model
2. A machine learning model based on markov chain.
3. Serve as standalone tweet generative model
4. Given a request, the model provides a tweet. Can be parameterized in future



# Build Docker
docker build -t autotweet .

# Run Docker
docker run -p 8000:8000 autotweet

# API Interface
http://0.0.0.0:8000
http://0.0.0.0:8000/tweet
http://0.0.0.0:8000/health
http://0.0.0.0:8000/docs