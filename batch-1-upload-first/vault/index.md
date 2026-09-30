# Personal Wiki Index

My course memory for **Fundamentals of Agentic AI** (Berkeley Haas, Fall 2026): the class slide decks and my own assignment write-ups, organized into linked notes. Start with [[Fundamentals of Agentic AI]] for the course map, or pick a topic below.

Every note ends with a **Sources** list that links back to the unchanged original in `raw/`. The [[Source Catalog]] maps each original file to the notes made from it.

## Course

_Class-by-class notes from the Fundamentals of Agentic AI slide decks._

- [[Class 1 - Code Foundations]] — Class 1, Code & Programming Foundations, focuses on prototyping with AI to build internal tools, A/B tests, and dashboards rather than becoming a software developer.
- [[Class 2 - Software Systems]] — Class 2, Software Systems, covers the process of turning a program into a product by detailing the product stack, including frontend, backend, databases, authentication, cloud deployment, and the assignment.
- [[Class 3 - Machine Learning]] — Class 3 covers machine learning foundations, focusing on how models are trained, the concept of generalization, evaluation, and the different learning paradigms including unsupervised and reinforcement learning, culminating in the Pac-Man project.
- [[Class 4 - Deep Learning and Transformers]] — Class 4 covers the progression from hand-designed features to learned representations using neural networks, embeddings, attention, and transformers, culminating in a tiny language model assignment.
- [[Class 5 - LLMs Prompting and Retrieval]] — This class covers LLM behavior, focusing on prompting techniques, context management, fine-tuning, and retrieval methods like RAG.
- [[Fundamentals of Agentic AI]] — Fundamentals of Agentic AI is a seven-class course; this wiki covers the first five, which move from code and programming through software systems, machine learning, and deep learning to LLM behavior, prompting, and retrieval.

## Projects

_My course assignments: what I built, the settings I chose, and what happened._

- [[Networking Tracker]] — The Networking Tracker is a private contact tracker designed for users at Berkeley, allowing each signed-in user to maintain isolated contact lists with features for adding, editing, sorting, and filtering contacts.
- [[Pac-Man DQN Agent]] — The Pac-Man DQN Agent was trained on Atari Ms. Pac-Man using three specific settings: exploration at 0.10, 300 episodes, and a learning rate of 0.0001.
- [[Personal Wiki Project]] — The Personal Wiki Project is a Class 5 assignment requiring the development of a personal wiki powered by a local model, retrieval, and chat/ask/search modes.
- [[Tiny nanoGPT Model]] — The Tiny nanoGPT Model refers to two word-level models trained from scratch using the nanoGPT framework, with identical settings; only the training corpus changed.

## Concepts

_Ideas that show up across classes and projects, explained with my own evidence._

- [[AI Coding Agents]] — AI Coding Agents are tools like Claude Code and OpenAI Codex that run in the terminal, capable of reading codebases, writing files, and running commands autonomously.
- [[APIs and HTTP]] — APIs function as agreements between systems, defining what callers can send and rely on receiving, while HTTP methods communicate the intent of those interactions.
- [[Authentication and Sessions]] — Authentication is crucial because without it, anyone can access any user's data, and it answers the question of whether a user is who they claim to be.
- [[Clean Code]] — Clean Code focuses on readability and maintainability by emphasizing principles like guard clauses, named constants, single-responsibility functions, and splitting projects by responsibility.
- [[Cloud Deployment]] — Cloud deployment involves moving a tested version of code into an environment, which requires managing different environments and planning for rollbacks.
- [[Context Windows]] — Context windows define the maximum amount of information, measured in tokens, a model can hold at once, which directly impacts its capacity for processing and memory.
- [[Databases and SQL]] — Databases organize records by defining a place for every record, where a database acts as an organized warehouse, and tables store facts while relationships connect them.
- [[Deep Q-Networks]] — Deep Q-Networks (DQN) use a neural network to estimate action values, replacing the traditional Q-table, allowing the agent to handle vast state spaces by processing input frames.
- [[Evaluation Design]] — Evaluation design involves using fixed seeds and evaluation suites, testing with small noisy samples, and utilizing public development tests to assess model performance.
- [[Fine-Tuning and LoRA]] — Fine-tuning and LoRA are methods used to adapt pretrained models, with fine-tuning permanently reshaping the model's distribution by changing its weights, while LoRA involves training a small add-on matrix (adapter) to nudge the model's behavior, offering a cheaper alternative to full fine-tuning.
- [[Git and GitHub]] — Git is a version control system that tracks every change to every file in a project, while GitHub is a cloud service that hosts Git repositories, enabling collaboration through features like Pull Requests.
- [[Hallucination]] — Hallucination occurs because fluent systems are designed to reward plausible continuation rather than guaranteeing source access or truth verification.
- [[Local Open Models]] — Local Open Models refer to open-weight models that can be run on a student's own hardware, which involves considerations for licensing, local inference setup, and memory calculations.
- [[Localhost and Ports]] — Localhost and ports are concepts related to running software on a machine, where localhost refers to the machine itself via the address 127.0.0.1, and ports act as identifiers for specific programs running on that machine.
- [[Model Training and Gradient Descent]] — Model training involves adjusting adjustable parameters of a model to fit historical examples by minimizing a loss function, often using gradient descent to iteratively improve predictions.
- [[Neural Networks]] — Neural Networks are small calculations inspired by biological neurons that receive inputs, multiply them by weights, add a bias, and pass the result through an activation function to produce an output score.
- [[Overfitting and Generalization]] — Overfitting and generalization relate to how a model fits training data, where overfitting occurs when a model fits training details that do not generalize, and bias and variance describe the systematic error and model flexibility, respectively.
- [[Precision and Recall]] — Precision and Recall are metrics used to count different types of mistakes made by a model, which is important because accuracy alone can hide errors depending on the cost associated with different types of errors.
- [[Prompt Engineering]] — Prompt Engineering involves guiding an LLM's output by adding detail, examples, constraints, and formatting requirements to steer the probability of a desired answer.
- [[Reinforcement Learning]] — Reinforcement Learning is a learning method where an agent learns a policy from experience and rewards to optimize its behavior.
- [[Retrieval Augmented Generation]] — Retrieval Augmented Generation (RAG) is a method that allows a Large Language Model (LLM) to access external, private data to ground its answers, addressing the limitation that an LLM's knowledge is frozen at its training data.
- [[Row Level Security]] — Row Level Security (RLS) in the Networking Tracker isolates each user's rows by implementing four policies for select, insert, update, and delete operations.
- [[Sampling Temperature]] — Sampling Temperature controls how random the output is by dividing the next-token scores before applying softmax, affecting the variety of generated text.
- [[Secrets and Environment Variables]] — Secrets and environment variables concern the practice of keeping sensitive information out of code, detailing which environment variables are public or server-only and the rationale behind this separation.
- [[Testing and CI]] — Testing and CI in JD's work focuses on treating tests as executable promises, using CI/CD as a release gate, and employing strategies like regression tests and the test pyramid.
- [[Tokens and Embeddings]] — Tokens are pieces into which text is broken by a tokenizer, and embeddings are learned vectors that represent words or tokens in a high-dimensional space.
- [[Training Loss Curves]] — Training loss curves in Pac-Man DQN showed that lower loss does not equate to better results, as loss can increase while performance fluctuates.
- [[Transformer Attention]] — Transformer Attention is a mechanism that allows a model to combine information from available token positions, replacing the sequential processing of RNNs.

---
_Updated by `wiki ingest` on 2026-09-30 04:52._
