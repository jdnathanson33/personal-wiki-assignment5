---
title: "Localhost and Ports"
description: "Localhost and ports are concepts related to running software on a machine, where localhost refers to the machine itself via the address 127.0.0.1, and ports act as identifiers for specific programs running on that machine."
type: concept
sources:
  - "[[raw/course-slides/haas-class1.html]]"
  - "[[raw/course-slides/haas-class2.html]]"
source_ids:
  - class1-slides
  - class2-slides
source_sha256:
  - class1-slides@f4383cbe1ffe
  - class2-slides@00a0281db897
model: gemma4:e2b-it-qat
execution: local
generated: 2026-09-29
reviewed: true
review_note: "Checked against sources by JD + Claude on 2026-09-29; see evidence/wiki-review.md"
---

# Localhost and Ports

Localhost and ports are concepts related to running software on a machine, where localhost refers to the machine itself via the address 127.0.0.1, and ports act as identifiers for specific programs running on that machine. This setup is crucial because a website is a running process, and localhost links only work on the local machine, not over the internet.

## Key details

- localhost is a name that always points back at the machine you are typing on, with the address 127.0.0.1, meaning "this computer" ([Class 1 slides (Code & Programming Foundations), slide 100: What localhost Actually Means](https://haas-ai-classes-fall-26.vercel.app/class1.html#/what-localhost-actually-means)).
- localhost requests, such as http://localhost:8000, never touch the internet; the request goes from the browser to another program on the same laptop and returns ([Class 1 slides (Code & Programming Foundations), slide 100: What localhost Actually Means](https://haas-ai-classes-fall-26.vercel.app/class1.html#/what-localhost-actually-means)).
- Ports function as apartment numbers for one address, indicating which program is being talked to; for example, localhost:8000 might be a Python’s built-in web server, while localhost:3000 might be a Node / React / Next.js dev server ([Class 1 slides (Code & Programming Foundations), slide 101: Ports: Apartment Numbers for One Address](https://haas-ai-classes-fall-26.vercel.app/class1.html#/ports-apartment-numbers-for-one-address)).
- The address is the building, and the port is the apartment; if an address is already in use, a different port must be used or the program must be stopped ([Class 1 slides (Code & Programming Foundations), slide 101: Ports: Apartment Numbers for One Address](https://haas-ai-classes-fall-26.vercel.app/class1.html#/ports-apartment-numbers-for-one-address)).
- Running a web server locally involves a process that starts and keeps running, waiting for requests, and each new line in the terminal log represents a request made by the browser ([Class 1 slides (Code & Programming Foundations), slide 99: Two Shapes of Software](https://haas-ai-classes-fall-26.vercel.app/class1.html#/two-shapes-of-software); [Class 1 slides (Code & Programming Foundations), slide 103: Why the Terminal “Freezes”](https://haas-ai-classes-fall-26.vercel.app/class1.html#/why-the-terminal-freezes)).
- A website is a process that must be running on a computer that is on; if the terminal is stopped (e.g., by Ctrl+C), the site cannot be reached even if the file remains on disk ([Class 1 slides (Code & Programming Foundations), slide 105: The Site Is a Process, Not a File](https://haas-ai-classes-fall-26.vercel.app/class1.html#/the-site-is-a-process-not-a-file)).
- localhost is not the internet; sending a localhost URL to someone else results in a connection error because the address points only to the local machine ([Class 1 slides (Code & Programming Foundations), slide 106: localhost Is Not the Internet](https://haas-ai-classes-fall-26.vercel.app/class1.html#/localhost-is-not-the-internet)).
- Localhost is used for testing, but it cannot be shared with others because the address points to the user's machine, not a public address ([Class 2 slides (Software Systems), slide 3: Localhost Is for Testing, But You Can’t Share It](https://haas-ai-classes-fall-26.vercel.app/class2.html#/localhost-is-for-testing-but-you-cant-share-it)).

## Related notes

- [[Class 1 - Code Foundations]] — taught here
- [[Cloud Deployment]] — how software leaves localhost
- [[Local Open Models]] — the local model server also runs on localhost

## Sources

- [[raw/course-slides/haas-class1.html|Class 1 slides (Code & Programming Foundations)]] — Two Shapes of Software, What localhost Actually Means, Ports: Apartment Numbers for One Address, Your First Web Server — Zero Dependencies, Why the Terminal “Freezes”, What Happens on Each Request, The Site Is a Process, Not a File, localhost Is Not the Internet · [public page](https://haas-ai-classes-fall-26.vercel.app/class1.html)
- [[raw/course-slides/haas-class2.html|Class 2 slides (Software Systems)]] — Localhost Is for Testing, But You Can’t Share It · [public page](https://haas-ai-classes-fall-26.vercel.app/class2.html)
