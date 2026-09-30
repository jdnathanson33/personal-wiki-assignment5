---
title: "Reinforcement Learning"
description: "Reinforcement Learning is a learning method where an agent learns a policy from experience and rewards to optimize its behavior."
type: concept
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

# Reinforcement Learning

Reinforcement Learning is a learning method where an agent learns a policy from experience and rewards to optimize its behavior. It involves defining states, actions, and rewards, and the objective is to maximize the expected cumulative reward rather than just the immediate reward.

## Key details

- State is where the agent is now, and Action is the move it chooses ([Class 3 slides (Machine Learning Foundations), slide 61: Actions Change What Happens Next](https://haas-ai-classes-fall-26.vercel.app/class3.html#/actions-change-what-happens-next)).
- Reward is feedback received after acting ([Class 3 slides (Machine Learning Foundations), slide 61: Actions Change What Happens Next](https://haas-ai-classes-fall-26.vercel.app/class3.html#/actions-change-what-happens-next)).
- In Reinforcement Learning, the agent learns a policy from experience and rewards ([Class 3 slides (Machine Learning Foundations), slide 61: Actions Change What Happens Next](https://haas-ai-classes-fall-26.vercel.app/class3.html#/actions-change-what-happens-next)).
- The objective is the expected cumulative reward, not the biggest reward on the next move ([Class 3 slides (Machine Learning Foundations), slide 62: Reward Now Versus Reward Later](https://haas-ai-classes-fall-26.vercel.app/class3.html#/reward-now-versus-reward-later)).
- Credit assignment is the process of determining which earlier action helped make a later outcome possible ([Class 3 slides (Machine Learning Foundations), slide 62: Reward Now Versus Reward Later](https://haas-ai-classes-fall-26.vercel.app/class3.html#/reward-now-versus-reward-later)).
- Q-Learning stores a value, $Q(s,a)$, which estimates the total discounted reward from a choice, used to follow the best-known choices ([Class 3 slides (Machine Learning Foundations), slide 63: Q-Learning Stores a Value for Each Action](https://haas-ai-classes-fall-26.vercel.app/class3.html#/q-learning-stores-a-value-for-each-action)).
- The Reward Defines What the Agent Optimizes, as the agent learns based on the reward structure provided ([Class 3 slides (Machine Learning Foundations), slide 67: The Reward Defines What the Agent Optimizes](https://haas-ai-classes-fall-26.vercel.app/class3.html#/the-reward-defines-what-the-agent-optimizes)).

## Related notes

- [[Class 3 - Machine Learning]] — taught here
- [[Deep Q-Networks]] — Q-learning with a neural network
- [[Pac-Man DQN Agent]] — my RL project

## Sources

- [[raw/course-slides/haas-class3.html|Class 3 slides (Machine Learning Foundations)]] — Actions Change What Happens Next, Reward Now Versus Reward Later, Q-Learning Stores a Value for Each Action, Exploration Collects New Experience, The Grid World Challenge, Try It: Train a Grid World Policy, The Reward Defines What the Agent Optimizes, A Q-Table Cannot List Every Game Screen · [public page](https://haas-ai-classes-fall-26.vercel.app/class3.html)
