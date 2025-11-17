# autotweet

The project is a dockerized REST API for tweet generation, using machine learning models based on Markov Chain and open-source LLM technology. It serves as a standalone model, providing on-demand tweet generation and allowing for easy parameterization for customization.

## Machine Learning
### Markov Chain

The tweet generation model is a custom-built Markov chain model trained using a public tweet dataset available on Kaggle (https://www.kaggle.com/kazanova/sentiment140). The model construction utilizes the pydtmc library, specifically leveraging the MarkovChain class.

#### Model Parameters:

- **Discrete-Time Markov Chain:** The model operates as a discrete-time Markov chain.
- **Size:** The size of the Markov chain is 1037, indicating the number of states or unique elements in the tweet dataset.
- **Rank:** The rank of the Markov chain is 1019, suggesting the complexity and depth of the model's transitions between states.
- **Classes:** The model has one class, indicating a singular behavior or sentiment category.
- **Recurrent & Transient States:** The model contains one recurrent state, indicating a state that the system returns to over time, while transient states are absent.
- **Ergodicity:** The Markov chain is ergodic, meaning it is both aperiodic and irreducible. Aperiodicity implies that the model does not follow a regular cycle, while irreducibility suggests that every state is reachable from every other state.
- **Absorbing States:** The model does not contain absorbing states, meaning once entered, the system does not remain in a particular state indefinitely.
- **Regularity:** The Markov chain is regular, indicating that every state has a positive probability of transitioning to every other state in a finite number of steps.
- **Reversibility & Symmetry:** The model is not reversible or symmetric, suggesting that the transition probabilities are not symmetric across states.

Overall, the model is designed to capture the dynamics and patterns present in the tweet dataset, allowing for the generation of new tweets that reflect the language and structure observed in the training data.

### Large Language Model (LLM)

It utilizes the GPT-2 model from Hugging Face for text generation tasks offline. This project aims to [state the main goal or purpose of your project].

#### Features

- **Text Generation**: Utilizes the GPT-2 model for generating human-like text.
- **Offline Usage**: The GPT-2 model is used offline, allowing for privacy and customizability.
- **Customizable Parameters**: Parameters such as `max_length`, `temperature`, `top_p`, and `do_sample` can be adjusted to control the behavior of text generation.
- **Easy Integration**: Can be easily integrated into existing projects or used as a standalone tool for text generation tasks.

#### Dependency

- [Hugging Face Transformers](https://github.com/huggingface/transformers)



## Poetry as Dependency Management 
poetry run python -m autotweet.app

## Poetry with uvicorn
poetry run uvicorn autotweet.app:app --reload

## Dockerization
docker build -t autotweet .

docker run -p 8000:8000 autotweet

## API Interface
http://0.0.0.0:8000/docs

## Other API Interface
1. http://0.0.0.0:8000
2. http://0.0.0.0:8000/docs
2. http://0.0.0.0:8000/tweet
3. http://0.0.0.0:8000/health
4. http://0.0.0.0:8000/docs
