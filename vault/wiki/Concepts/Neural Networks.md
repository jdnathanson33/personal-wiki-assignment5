---
title: "Neural Networks"
description: "Neural Networks are small calculations inspired by biological neurons that receive inputs, multiply them by weights, add a bias, and pass the result through an activation function to produce an output score."
type: concept
sources:
  - "[[raw/course-slides/haas-class4.html]]"
source_ids:
  - class4-slides
source_sha256:
  - class4-slides@6091b9482247
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Neural Networks

Neural Networks are small calculations inspired by biological neurons that receive inputs, multiply them by weights, add a bias, and pass the result through an activation function to produce an output score. They are crucial because stacking these units allows models to combine features, and the training process involves adjusting parameters and hyperparameters to learn from data.

## Key details

- An artificial neuron receives inputs, multiplies each input by its weight, adds the results, and adds a bias before applying an activation function ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 9: The Artificial Neuron](https://haas-ai-classes-fall-26.vercel.app/class4.html#/the-artificial-neuron)).
- The formula for a neuron is output = activation(weight₁ × input₁ + weight₂ × input₂ + bias), where weights control input influence, bias shifts the calculation, and activation bends the response ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 11: The Neuron as a Formula](https://haas-ai-classes-fall-26.vercel.app/class4.html#/the-neuron-as-a-formula)).
- Weights control how an input changes a neuron's calculation, and they can be positive, negative, or near zero ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 11: The Neuron as a Formula](https://haas-ai-classes-fall-26.vercel.app/class4.html#/the-neuron-as-a-formula)).
- The bias shifts the calculation, similar to an intercept in a regression ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 11: The Neuron as a Formula](https://haas-ai-classes-fall-26.vercel.app/class4.html#/the-neuron-as-a-formula)).
- The activation function bends the response, and the result is passed to the next layer ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 11: The Neuron as a Formula](https://haas-ai-classes-fall-26.vercel.app/class4.html#/the-neuron-as-a-formula)).
- One neuron produces one feature, and connecting many neurons allows the model to combine features ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 9: The Artificial Neuron](https://haas-ai-classes-fall-26.vercel.app/class4.html#/the-artificial-neuron)).
- A single neuron's output score is passed through a sigmoid function, resulting in a score between 0 and 1 ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 10: A Single Neuron in Action](https://haas-ai-classes-fall-26.vercel.app/class4.html#/a-single-neuron-in-action)).
- The network learns parameters, which include connection weights and neuron biases, such as the 26 learned parameters in a small network ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 18: What’s Actually Being Adjusted?](https://haas-ai-classes-fall-26.vercel.app/class4.html#/whats-actually-being-adjusted); [Class 4 slides (Deep Learning, Embeddings & Transformers), slide 19: Parameters vs Hyperparameters](https://haas-ai-classes-fall-26.vercel.app/class4.html#/parameters-vs-hyperparameters)).
- Hyperparameters chosen for training include the number of layers and neurons, the activation function, the learning rate, and the training duration ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 19: Parameters vs Hyperparameters](https://haas-ai-classes-fall-26.vercel.app/class4.html#/parameters-vs-hyperparameters)).
- The training loop involves a forward pass, loss calculation, backward pass, and update step, where only the update step changes the parameters ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 17: The Training Loop](https://haas-ai-classes-fall-26.vercel.app/class4.html#/the-training-loop)).
- Backpropagation calculates how a small change to each setting would change the loss, and the optimizer uses these gradients to adjust the weights and biases ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 16: How a Neural Network Learns](https://haas-ai-classes-fall-26.vercel.app/class4.html#/how-a-neural-network-learns)).
- Parameters are adjusted by choosing a connection and moving its weight, while the input data remains fixed ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 18: What’s Actually Being Adjusted?](https://haas-ai-classes-fall-26.vercel.app/class4.html#/whats-actually-being-adjusted)).

## Related notes

- [[Class 4 - Deep Learning and Transformers]] — taught here
- [[Model Training and Gradient Descent]] — the same update idea
- [[Transformer Attention]] — transformers are neural networks
- [[Deep Q-Networks]] — a network estimates action values

## Sources

- [[raw/course-slides/haas-class4.html|Class 4 slides (Deep Learning, Embeddings & Transformers)]] — The Artificial Neuron, A Single Neuron in Action, The Neuron as a Formula, Why Nonlinearity Matters, Inspired by the Brain, A Brain and a Neural Network, One Neuron → A Network, How a Neural Network Learns · [public page](https://haas-ai-classes-fall-26.vercel.app/class4.html)
