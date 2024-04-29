import os
import pickle
from abc import ABC


class Tweeter(ABC):

    def tweet(self) -> str:
        ...

    @staticmethod
    def process_tweet(tweet: str) -> str:
        return tweet


class LLMTweeter(Tweeter):
    def __init__(self):
        super().__init__()

    def tweet(self) -> str:
        return Tweeter.process_tweet("Static tweet")


class MarkovChainTweeter(Tweeter):

    def __init__(self, path: str = 'model/markov-chain.pkl'):
        if not os.path.exists(path):
            raise FileNotFoundError(f"The model at {path} does not exist.")
        with open(path, 'rb') as model:
            self.markov_chain = pickle.load(model)

    def tweet(self) -> str:
        return Tweeter.process_tweet(" ".join(self.markov_chain.simulate(15)))


class TweeterFactory:
    @staticmethod
    def create_instance(model_name="markovchain") -> Tweeter:
        if model_name == 'markovchain':
            return MarkovChainTweeter()
        elif model_name == 'llm':
            return LLMTweeter()
        else:
            raise ValueError("Invalid choice")
