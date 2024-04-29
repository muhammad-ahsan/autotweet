import json
import pickle
import random
import uuid
from datetime import datetime

import uvicorn
from fastapi import FastAPI

app = FastAPI()


def post_processing_tweet( post: str ):
    emojis = [' !', ' ....', ' ;)', ' :(']
    end = random.sample(emojis, 1)[0]
    return post[0].upper() + post[1:] + end


def load_mode():
    with open('model/markov-chain.pkl', 'rb') as model:
        return pickle.load(model)


markov_chain = load_mode()


@app.get("/")
async def root():
    return {"message": "Welcome to auto tweet generator API"}


@app.get("/tweet")
async def predict():
    tweet = post_processing_tweet(' '.join(markov_chain.simulate(15)))
    return json.dumps({"timestamp": str(datetime.now()),
                       "response_id": str(uuid.uuid4()),
                       "tweet": tweet})


@app.get("/health")
async def health():
    return {"message": "Congratulations, I am healthy :) "}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
