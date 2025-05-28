# Not Just a Chatbot — A Fintech Assistant

> *What if you had a financial analyst who never gets tired of reading reports, never forgets who was wrong and when, and isn’t afraid to admit they were mistaken?  
I'm designing an investment assistant that won't just scrape stock data but will analyse it in context, remember conclusions, compare scenarios, and learn over time.  
This isn’t a release note — it’s a concept. An architecture. A little insight into why the project makes sense at all.  
I believe it’ll be of interest to anyone who values thoughtful long-term investing — and is fed up with the AI hype train (because nowadays, everyone seems to slap those two letters on anything just for clout).*

---
## Introduction

The system currently known under the working title *Project S* is my pet project and a personal experiment in investment analytics and artificial intelligence.  
It’s not an algorithmic trader, not a Telegram signal bot, and certainly not just another screener where someone let AI loose on financial metrics.  
It’s an attempt to gather scattered information flows — news, reports, forecasts, press releases, analysts’ opinions — and turn them into a system that helps invest long-term, thoughtfully, and meaningfully.

---

## What Prompted Me to Create This project

Clearly, today's AI and machine learning systems can process vast amounts of data and identify patterns in unstructured information much faster than any human. But they have some serious limitations that currently prevent them from replacing a real financial analyst or portfolio manager.
1. Perhaps such systems exist, but I haven’t seen any tools that can truly process and cross-reference data from multiple formats and sources — PDFs, spreadsheets, images, spoken word, trade journals, press releases, and more.
2. Obviously, computer systems lack intuition or “market instinct,” so they won’t sense when a picture-perfect investment feels off — that subtle alarm bell an experienced human might pick up on, which often proves right.
3. No matter how refined an algorithm is, it’s still created by humans. AI can only operate within the logic it was given. And since we humans are fallible by nature, so too are our creations.
I’m not naïve enough to think I can overcome all of these issues working solo on *Project S*, but maybe — just maybe — I can close a few of the gaps. So this project is conceived as a system that will:
- Analyse data from multiple formats and sources;
- Make recommendations based on prior experience and an ever-growing knowledge base;
- Remember the context in which past decisions were made;
- Try to spot anomalies based on accumulated experience;
- And use that knowledge to improve outcomes, not just repeat old mistakes.

Another thing worth mentioning. If you’ve browsed Medium or any tech blog recently, you’ve probably seen articles like:
> *“I built an AI that beats the market by 100% and now I’m filthy rich!”*
What that usually means is: someone fed ChatGPT or another LLM some data from the Yahoo Finance API and crafted a fancy prompt asking it to act like a financial analyst and recommend whether or not to buy a particular stock. And because there’s a fancy LLM under the hood, they shamelessly call the result “AI-driven analysis.” But does that really turn the LLM into a trustworthy analyst? I may be wrong, but with a clear understanding of how LLMs and transformers work — I wouldn’t trust such gimmicks with my own money.

**This project is a different beast entirely.**  
It’s being designed as a system that:
- Doesn’t just collect data — it semantically analyses everything: news, press releases, financial reports, media, and forecasts;
- Remembers decisions and the context in which they were made;
- Retrospectively evaluates source reliability and adjusts weightings accordingly;
- Learns from its own conclusions — and grows over time.

---

## Why I Started with Architecture, Not Code

You won’t find any code snippets in this article — simply because I haven’t written them yet. I started with architecture because I knew that if I wanted to build a system that would:  
- Analyse information from different media types,  
- Learn from both its own and others’ experience,  
- Be stable and scalable,  
— I had to lay out a structure that could actually support all of that. That’s how I arrived at C4 modelling.

---

## Minimal Stack, Zero Hype

I gave myself a clear goal: **minimum tech — maximum outcome.**
- Python — the core language.
- MySQL — reliable relational database.
- Qdrant — for storing context and semantic vectors.
- Docker — for containerised modular architecture.
- FastAPI/Flask — to wrap modules with lightweight interfaces.
- Celery + Redis — to orchestrate tasks and processes.

I'm not chasing shiny frameworks — I’m building a system that I can maintain, expand, and scale myself. And if one day I decide to throw in computer vision or chart parsing — I won’t have to rewrite everything from scratch.

---

## What project Is Made Of

*Project S* isn’t a monolith — it’s a set of interconnected modules, each responsible for a focused task. Together, they form a system that can:
•	Ingest data in any format,  
•	Transform it into text/vectors/metrics,  
•	Apply various advanced analytical methods,  
•	Track what conclusions were made and under what conditions,  
•	Deliver results in a clear and useful form.

Here’s a quick overview of the modules I’m building.

### 1. Input Modules
- **API Gateways**: Fetch data not just from financial APIs but also from news aggregators, YouTube, Gmail, and Telegram bots (to which you can forward a message or file).
- **Downloader**: Downloads files — attachments from emails or videos from Telegram.
- **File Service**: Handles user uploads through the web interface or mobile app (once it’s live).

---
### 2. Cleaning and Routing
- **Security Scanner**: Scans files for safety.
- **Data Orchestrator**: Determines input type and routes it to the appropriate processor.
- All of this runs through a task queue and is scalable as the load increases.

---

### 3. Data Processing
- **Media Processing**: Converts video/audio to text using OpenAI Whisper and other LLMs.
- **PDF/Text Processing**: Extracts and cleans text from documents, press releases, emails, messages, and so on.

---

### 4. Semantic Analysis
- **News Analysis**: Applies ML to news articles to extract key semantic patterns.
- **Media Analysis**: Same job, but for podcasts, videos, and other media.
- **Report Analysis**: Uses ML to interpret financial reports, extracting core meanings and insights.
- **Forecast Evaluation**: Gathers forecasts from news and analysts, tracks their accuracy over time, and builds a trustworthiness matrix while storing semantic embeddings.

---

### 5. Mathematical Analysis
There are eight sequential modules, each dedicated to a specific analytical stage:
- Filtering stocks by key metrics,
- Risk assessment,
- Growth and efficiency evaluation,
- Profitability forecasting,
- Stress testing,
- Break-even analysis,
- Simulations and regressions,
- Final selection and scoring.

---

### 6. Final Output Correction
- **Analysis Correction**: The final checkpoint. It adjusts conclusions from the mathematical block, based on:
  - Semantic insights from media sources,
  - Accumulated memory (RAG),
  - Reliability and reputation of those who previously made forecasts.

---

### 7. Memory: The RAG Mechanism
- **ragMemory**: A self-learning module that remembers which conclusions were drawn in which context — and compares current situations to past cases when appropriate.

---

### 8. User Interface
- **Web UI**: Displays analytics, visualisations, and recommendations.
- **Assistant**: An AI chat assistant (planned after web UI), allowing the user to communicate with the system in a conversational way.
- **Mobile App**: Will eventually mirror the web experience and bring it to your pocket.

---

### 9. Supporting Modules
- **Event Service**: Allows modules to listen and react to each other's triggers.
- **Notification Service**: For emails, Telegram alerts, or push notifications (for future mobile use).
- **Logging & Semantic Logs**: Logs system behaviour and can semantically vectorise it for analysis and anomaly detection.
- **Subscription Service**: Manages access levels and will be used later for monetisation.

---

## 10. How Everything Is Stored — From Metrics to Memory Vectors
Once the system deals with dozens of data sources and thousands of conclusions, it’s no longer just about “where data is kept,” but *how* it’s organised.
The *Project S* will use two main storage types: classical relational (MySQL) and vector-based (Qdrant).

---

### A. Relational Storage (MySQL)
Used for structured, transactional data:
- **Market data**: Historical prices, financial ratios, API-fed metrics.
- **User data**: Preferences, portfolios, wishlists, integration settings.
- **Mathematical analysis results**: From initial filters to final scoring.
- **Notifications and events**: For syncing, retries, and scheduling.
- **Logs**: System events, user actions, errors — all the usual suspects.

---

### B. Vector Storage (Qdrant)
Used where *meaning* matters more than structure:
- **newsdata**: Vectors representing article tone and themes.
- **mediaData**: Semantic encodings of podcasts, videos, etc.
- **forecastData**: Forecast vectors — company, timing, accuracy.
- **stockResultAnalysis**: Final stock assessment embeddings.
- **logsSemanticStorage**: Vectorised logs for pattern/anomaly analysis.
- **ragMemoryStorage**: The brain — stores experiences and the context they were formed in. This is where *Project S* learns from the past.

---

### Why This Combo?
- **MySQL**: Structure, reliability, transactional safety.
- **Qdrant**: Flexibility, semantics, vector-based intuition.
Together, they make the system both logical and insightful — equally fluent in numbers and nuance.

---

## Memory as a Thinking Tool: Why project Needs RAG

I’m no Wall Street pro — just a nerd who’s tried plenty of retail investor tools. And you know what? Most of them don’t remember anything. Every time you hit “analyse,” they start from scratch. They don’t *learn*.
*Project S* is built differently. It remembers — thanks to RAG (Retrieval-Augmented Generation). What this means, in plain English, is:
- The system stores experience (not just data).
- When a new situation arises, it can search for similar past cases.
- It can compare how it reacted back then.
- It can adjust its current response accordingly.
This is implemented via the `ragMemory` module and its `ragMemoryStorage` brain, powered by Qdrant.

---

### What Gets Stored in Memory?
Every time the system generates a conclusion (like a stock recommendation), it stores:
- The context — relevant news, reports, forecasts.
- The numerical metrics involved.
- The source accuracy scores.
- And the final decision.

These turn into a vector of experience. When a similar situation occurs, the system can:
- Recall its previous action and rationale.
- Revise its current assessment.
- Or, if needed, consciously choose a new path.

---

### Why Does It Matter?
This approach allows the system to:
- Not just store data, but actually *learn* from experience;
- Avoid forgetting processed insights;
- Grow more insightful and grounded with every cycle.
It’s a step toward transforming project from a glorified algorithm into a genuine AI investing assistant. Not a wizard — but a reliable second opinion that evolves with its users.

---

## How Users Will Interact: Assistant, Visuals, and Just a Touch of Magic
*Project S* won’t just gather and analyse — it’ll explain. No raw ratios or prediction blurbs. Instead, it’ll provide clear, structured responses to vital questions:
- What’s happening with this stock?
- What risks does this company carry?
- Who forecasted what, and were they right?
- What happened in similar past cases?

---

### Assistant: Conversational, Not Chatty
Once the web UI is sorted, I’ll build the assistant. A chat interface where users can:
- Ask questions,
- Request an explanation for a result,
- Drill down: “Show me why you concluded that.”

This isn’t just an LLM slapped on the frontend. It’s a transparent interface wired into the memory, logic, maths, and data underneath. If the assistant says something — it’ll be able to explain *why* it said that. No hallucinations. Just explainable logic.
Every answer will be traceable: which sources, which memory entries, which metrics influenced it. Not a black box — more like a glass assistant with annotated footnotes.

---

### Visualisation: Numbers ≠ Insight
There’ll be a dedicated module for building:
- Time series and financial charts,
- Event maps and relationships,
- Aggregated summaries from multiple sources.

So instead of “This stock has a P/E of 14.7,” users will see the whole story — patterns, spikes, contradictions, all in one place.

---

### Web and Mobile App
The web UI is priority #1. But a mobile client is already accounted for in the C4 diagram — it’ll come later.

---

## Subscription and API Access: Who Is This For?

*Project S* is for thoughtful, long-term investors. Not hype-chasers, not signal hunters. 
The monetisation model will likely be subscription-based. I haven’t decided on details yet, but a dedicated access module is already included.

---

### External API
If the project reaches an enterprise scale, I might open a paid analytics API:
- For platform integration, portfolio systems, or terminals.
- The architecture already includes a data gateway with auth, logging, and access levels.

---

## Will project Be Sold as a Product?

At this point — probably not. It’s not being built as a showroom or something to parade. It’s a tool — built for myself and for people who think like I do. Maybe someday there will be partners, funds, or integrators who’ll want access. But for now, *Project S* remains an engineering pet-project with a very real purpose. Not a pitch deck — but a thinking machine. *Project S* is not a startup for me. It’s a different way of thinking. I’m not building some almighty algorithmic guru powered by ML and LLMs that magically predicts which stocks will fly or crash tomorrow. I’m designing a system that supports long-term decision-making — rooted in context, accumulated experience, and structured analysis.
*Project S* doesn’t aspire to be a crystal ball. It won’t tell you what you want to hear. It will show patterns, raise flags, and help you understand what’s going on — and whether action is needed.
This is not a hype machine. If you're looking for yet another scheme promising fast and massive profits — keep scrolling. This isn’t for you. And frankly, you’re not for me.
I’m building a stable, resilient system — not for a flashy demo or a startup grant, but first and foremost as a working tool for myself. If it happens to be useful to others — brilliant!
That said, progress is slow. Like any solid structure, this one is being built step by step: first comes logic, then the architectural foundation, then the module spectrum, and only then — the code.
At the very beginning of this article, I explained why no existing system can truly replace a seasoned portfolio manager. *Project S* won’t be that replacement either. But I do hope it becomes a second voice — one that remembers, analyses, resists illusions, and, when the moment comes, is ready to say: “Hold up, mate. We’ve been here before. And here’s how it turned out last time.”

---

## What’s Next?

Based on everything above, *Project S* is being created as a full-fledged AI investment assistant — with the long-term potential to evolve into a semi-autonomous fintech agent.
But that’s for the future. For now, it’s moving slowly from my brain to my machine — and eventually, to the public.

Next steps:
- Set up the dev and local production environments;
- Build the MVP module set;
- Set up a basic local CI/CD pipeline.

🙏 If you’ve made it this far, thank you sincerely. 
I know this took time — and I truly appreciate you spending it to understand the architecture and soul of my project.
If you have feedback, ideas, or just want to chat — I’d love to hear it.

It’s all good.  
Peace!
