---
title: "Class 4 - Deep Learning and Transformers"
description: "Class 4 covers the progression from hand-designed features to learned representations using neural networks, embeddings, attention, and transformers, culminating in a tiny language model assignment."
type: course
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

# Class 4 - Deep Learning and Transformers

Class 4 covers the progression from hand-designed features to learned representations using neural networks, embeddings, attention, and transformers, culminating in a tiny language model assignment. This material focuses on how deep learning learns intermediate features and how language models function as predictions.

## Key details

- Deep learning learns multiple layers of representation, where pixel values transform into simple patterns, combinations, and predictions ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 5: Deep Learning Learns Multiple Layers of Representation](https://haas-ai-classes-fall-26.vercel.app/class4.html#/deep-learning-learns-multiple-layers-of-representation)).
- A neural network functions by turning input numbers into output numbers using adjustable weights and biases, and training involves changing parameters to reduce loss on examples ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 6: A Neural Network Is Still a Function](https://haas-ai-classes-fall-26.vercel.app/class4.html#/a-neural-network-is-still-a-function)).
- The roadmap for the class includes understanding one neuron, a network learning intermediate features, training by predicting and measuring loss, and exploring language concepts like tokens, embeddings, attention, and transformers ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 7: Today’s Roadmap](https://haas-ai-classes-fall-26.vercel.app/class4.html#/todays-roadmap)).
- Language model training rewards predicting text, and a confident prediction does not verify the answer, as it can produce plausible but incorrect facts ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 70: A Fluent Answer Is Still a Prediction](https://haas-ai-classes-fall-26.vercel.app/class4.html#/a-fluent-answer-is-still-a-prediction)).
- The assignment requires choosing text, training a supplied tiny language model (using Karpathy’s nanoGPT in PyTorch), and explaining the changes using outputs ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 73: Assignment 3: Train Your Own Tiny LLM](https://haas-ai-classes-fall-26.vercel.app/class4.html#/assignment-3-building-a-custom-llm)).
- During the assignment, one should inspect five examples from the corpus to explain what patterns they could teach ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 74: Run It, Then Inspect What Changed](https://haas-ai-classes-fall-26.vercel.app/class4.html#/open-the-notebook-and-make-three-choices)).
- Embeddings are learned vectors, and token IDs are lookup indices, while the corpus and IDs remain fixed during training, and training changes the learned parameters ([Class 4 slides (Deep Learning, Embeddings & Transformers), slide 74: Run It, Then Inspect What Changed](https://haas-ai-classes-fall-26.vercel.app/class4.html#/open-the-notebook-and-make-three-choices)).

## Related notes

- [[Fundamentals of Agentic AI]] — course map
- [[Neural Networks]] — covered in this class
- [[Tokens and Embeddings]] — covered in this class
- [[Transformer Attention]] — covered in this class
- [[Tiny nanoGPT Model]] — the assignment for this class
- [[Class 3 - Machine Learning]] — previous class
- [[Class 5 - LLMs Prompting and Retrieval]] — next class

## Sources

- [[raw/course-slides/haas-class4.html|Class 4 slides (Deep Learning, Embeddings & Transformers)]] — From Hand-Designed Features to Learned Representations, Class 3 Recap: In Sixty Seconds, The Limitation of Classic ML, Deep Learning Learns Multiple Layers of Representation, A Neural Network Is Still a Function, Today’s Roadmap, A Fluent Answer Is Still a Prediction, Assignment 3: Train Your Own Tiny LLM · [public page](https://haas-ai-classes-fall-26.vercel.app/class4.html)
