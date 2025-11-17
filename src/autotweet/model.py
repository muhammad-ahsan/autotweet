import os
import string
import pickle
from abc import ABC

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


class Tweeter(ABC):

    def __init__(self, tweet_size: int = 20):
        self.default_tweet_size = tweet_size

    def tweet(self) -> str:
        ...

    def process_tweet(self, tweet: str) -> str:
        return tweet


class LLMTweeter(Tweeter):

    def __init__(self):
        super().__init__()
        self._model_dir = "models/gpt2"
        if not os.path.exists(self._model_dir):
            print("Model does not exist. Downloading model...")

            # Download the tokenizer and model
            self._tokenizer = GPT2Tokenizer.from_pretrained(f"gpt2")
            self._model = GPT2LMHeadModel.from_pretrained(f"gpt2")
            # Save the tokenizer and model to a specific directory
            self._tokenizer.save_pretrained(self._model_dir)
            self._model.save_pretrained(self._model_dir)
        else:
            print("Model already exists. Loading model...")
            self._tokenizer = GPT2Tokenizer.from_pretrained(self._model_dir)
            self._model = GPT2LMHeadModel.from_pretrained(self._model_dir)

        # Set the device to use (CPU or GPU)
        self._device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print("DEVICE: ", self._device)
        self._model.to(self._device)
        self._prompt = "Generate some scientific information:"

    def tweet(self) -> str:

        input_ids = self._tokenizer.encode(self._prompt, return_tensors="pt").to(self._device)
        output = self._model.generate(input_ids=input_ids,
                                      max_length=50,
                                      temperature=0.7,
                                      top_p=0.9,
                                      do_sample=True)

        # Decode the generated output
        generated_text = self._tokenizer.decode(output[0], skip_special_tokens=True)
        return self.process_tweet(generated_text)

    def process_tweet(self, tweet: str) -> str:
        clean_tweet = tweet.replace(self._prompt, "")
        clean_tweet.translate(str.maketrans('', '', string.punctuation))
        sentences = clean_tweet.split("\n")
        unique_sentences = list(set(sentences))
        return " ".join(unique_sentences)


class MarkovChainTweeter(Tweeter):

    def __init__(self, path: str = 'models/markov-chain/markov-chain.pkl'):
        super().__init__()
        if not os.path.exists(path):
            raise FileNotFoundError(f"The models at {path} does not exist.")
        with open(path, 'rb') as model:
            self.markov_chain = pickle.load(model)

    def tweet(self) -> str:
        return self.process_tweet(" ".join(self.markov_chain.simulate(self.default_tweet_size)))


class TweeterFactory:
    @staticmethod
    def create_instance(model_name="llm") -> Tweeter:
        if model_name == 'markovchain':
            return MarkovChainTweeter()
        elif model_name == 'llm':
            return LLMTweeter()
        else:
            raise ValueError("Invalid choice")
