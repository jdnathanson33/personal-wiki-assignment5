---
title: "Class 2 - Software Systems"
description: "Class 2, Software Systems, covers the process of turning a program into a product by detailing the product stack, including frontend, backend, databases, authentication, cloud deployment, and the assignment."
type: course
sources:
  - "[[raw/course-slides/haas-class2.html]]"
source_ids:
  - class2-slides
source_sha256:
  - class2-slides@00a0281db897
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Class 2 - Software Systems

Class 2, Software Systems, covers the process of turning a program into a product by detailing the product stack, including frontend, backend, databases, authentication, cloud deployment, and the assignment. This material outlines the steps from local testing to deploying a live, shareable application.

## Key details

- The process of moving from localhost testing to a real URL involves having a browser ask for a page and a machine answer it, where the difference is who is answering ([Class 2 slides (Software Systems), slide 4: What Happens When You Type a URL](https://haas-ai-classes-fall-26.vercel.app/class2.html#/what-happens-when-you-type-a-url)).
- The frontend is what users interact with in a browser, while the backend is the machine that answers the request ([Class 2 slides (Software Systems), slide 4: What Happens When You Type a URL](https://haas-ai-classes-fall-26.vercel.app/class2.html#/what-happens-when-you-type-a-url)).
- Databases provide the application's durable memory and fast temporary storage, and can include options like PostgreSQL, MongoDB, or Redis ([Class 2 slides (Software Systems), slide 34: What Is a Tech Stack?](https://haas-ai-classes-fall-26.vercel.app/class2.html#/what-is-a-tech-stack)).
- Secrets and authentication are mechanisms that allow the system to know who is making a request ([Class 2 slides (Software Systems), slide 4: What Happens When You Type a URL](https://haas-ai-classes-fall-26.vercel.app/class2.html#/what-happens-when-you-type-a-url)).
- Cloud and deployment describe how the application comes into existence ([Class 2 slides (Software Systems), slide 4: What Happens When You Type a URL](https://haas-ai-classes-fall-26.vercel.app/class2.html#/what-happens-when-you-type-a-url)).
- A tech stack is defined as the combination of technologies used to build and run an application ([Class 2 slides (Software Systems), slide 34: What Is a Tech Stack?](https://haas-ai-classes-fall-26.vercel.app/class2.html#/what-is-a-tech-stack)).
- The assignment requires building a networking tracker using the stack: Next.js + Supabase + Vercel ([Class 2 slides (Software Systems), slide 46: The Assignment](https://haas-ai-classes-fall-26.vercel.app/class2.html#/the-assignment)).
- The definition of done includes having the app live on a public URL, supporting user sign-in/sign-out, ensuring data privacy between users, validating inputs, and having at least one automated test pass ([Class 2 slides (Software Systems), slide 47: Definition of Done: Your Rubric](https://haas-ai-classes-fall-26.vercel.app/class2.html#/definition-of-done-your-rubric)).

## Related notes

- [[Fundamentals of Agentic AI]] — course map
- [[APIs and HTTP]] — backend concept from this class
- [[Databases and SQL]] — data layer from this class
- [[Authentication and Sessions]] — auth from this class
- [[Cloud Deployment]] — deployment from this class
- [[Networking Tracker]] — the assignment for this class
- [[Class 1 - Code Foundations]] — previous class
- [[Class 3 - Machine Learning]] — next class

## Sources

- [[raw/course-slides/haas-class2.html|Class 2 slides (Software Systems)]] — Localhost Is for Testing, But You Can’t Share It, What Happens When You Type a URL, The Product Stack, Today’s Agenda, What Is a Tech Stack?, The Assignment, Definition of Done: Your Rubric · [public page](https://haas-ai-classes-fall-26.vercel.app/class2.html)
