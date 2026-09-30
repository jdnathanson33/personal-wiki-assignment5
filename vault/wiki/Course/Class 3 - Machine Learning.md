---
title: "Class 3 - Machine Learning"
description: "Class 3 covers machine learning foundations, focusing on how models are trained, the concept of generalization, evaluation, and the different learning paradigms including unsupervised and reinforcement learning, culminating in the Pac-Man project."
type: course
sources:
  - "[[raw/course-slides/haas-class3.html]]"
source_ids:
  - class3-slides
source_sha256:
  - class3-slides@0468e12c46ef
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Class 3 - Machine Learning

Class 3 covers machine learning foundations, focusing on how models are trained, the concept of generalization, evaluation, and the different learning paradigms including unsupervised and reinforcement learning, culminating in the Pac-Man project. It emphasizes that machine learning involves training a model on past usage and outcomes to predict future results.

## Key details

- Machine learning involves using past usage and renewal outcomes to train a learned model to predict renewal estimates for a new account ([Class 3 slides (Machine Learning Foundations), slide 8: Last Class We Wrote the Rules](https://haas-ai-classes-fall-26.vercel.app/class3.html#/last-class-we-wrote-the-rules)).
- Training fits the model’s settings by choosing the inputs and objective ([Class 3 slides (Machine Learning Foundations), slide 8: Last Class We Wrote the Rules](https://haas-ai-classes-fall-26.vercel.app/class3.html#/last-class-we-wrote-the-rules)).
- A learned model captures useful patterns from training examples in its parameters, allowing it to make predictions about new examples, provided the learned patterns still apply when the situation changes ([Class 3 slides (Machine Learning Foundations), slide 11: Condensation of Knowledge](https://haas-ai-classes-fall-26.vercel.app/class3.html#/condensation-of-knowledge)).
- The first half of the class covers AI history and the landscape and checks whether learning generalizes ([Class 3 slides (Machine Learning Foundations), slide 16: Today’s Route](https://haas-ai-classes-fall-26.vercel.app/class3.html#/todays-route)).
- The class route includes defining the prediction and preparing data, comparing models and evaluating errors, fitting a model by reducing loss, finding clusters without labels (unsupervised learning), choosing actions through reinforcement learning, and training a Grid World policy, then starting Pac-Man ([Class 3 slides (Machine Learning Foundations), slide 16: Today’s Route](https://haas-ai-classes-fall-26.vercel.app/class3.html#/todays-route)).
- Three ways a machine can learn are Supervised learning (inputs + known answers to predict an answer), Unsupervised learning (inputs without answers to find structure), and Reinforcement learning (an environment + rewards to choose actions over time) ([Class 3 slides (Machine Learning Foundations), slide 18: Three Ways a Machine Can Learn](https://haas-ai-classes-fall-26.vercel.app/class3.html#/three-ways-a-machine-can-learn)).
- The Pac-Man project involves training an agent to play Ms. Pac-Man by choosing exploration, episodes, and learning rate, and watching gameplay to compare before/after scores ([Class 3 slides (Machine Learning Foundations), slide 70: Train an Agent to Play Ms. Pac-Man](https://haas-ai-classes-fall-26.vercel.app/class3.html#/train-an-agent-to-play-ms.-pac-man)).
- Evaluation for the Pac-Man project requires submitting a notebook with the three chosen hyperparameters, an untrained GIF, later checkpoints, a training plot, and a comparison of five evaluation games with the untrained baseline ([Class 3 slides (Machine Learning Foundations), slide 71: Show What the Agent Actually Learned](https://haas-ai-classes-fall-26.vercel.app/class3.html#/show-what-the-agent-actually-learned)).

## Related notes

- [[Fundamentals of Agentic AI]] — course map
- [[Model Training and Gradient Descent]] — core training idea from this class
- [[Overfitting and Generalization]] — model choice from this class
- [[Precision and Recall]] — evaluation from this class
- [[Reinforcement Learning]] — RL from this class
- [[Pac-Man DQN Agent]] — the assignment for this class
- [[Class 2 - Software Systems]] — previous class
- [[Class 4 - Deep Learning and Transformers]] — next class

## Sources

- [[raw/course-slides/haas-class3.html|Class 3 slides (Machine Learning Foundations)]] — Last Class We Wrote the Rules, Why Can’t We Just Code All the Rules?, AI Feels Like an Alien Oracle…, Condensation of Knowledge, Today’s Route, Three Ways a Machine Can Learn, Train an Agent to Play Ms. Pac-Man, Show What the Agent Actually Learned · [public page](https://haas-ai-classes-fall-26.vercel.app/class3.html)
