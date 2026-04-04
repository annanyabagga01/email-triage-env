---
title: Email Triage Env
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_file: inference.py
pinned: true
---
# 📧 Email Triage AI Environment

## 🚀 Overview

This project simulates a real-world **Email Management System** where an AI agent learns to intelligently process incoming emails.

The environment is designed following a **step-based interaction model**, similar to reinforcement learning environments, where an agent observes, acts, and receives rewards.

---

## 🧠 Problem Statement

Organizations receive thousands of emails daily. Automating:

* spam detection
* department routing
* response generation

can significantly improve efficiency.

---

## ⚙️ Tasks

### 1. Spam Detection

Classify emails as:

* spam
* not spam

### 2. Email Routing

Route emails to appropriate departments:

* Tech
* Billing
* HR

### 3. Reply Generation

Generate helpful and polite responses based on the email content.

---

## 🎯 Reward Design

| Task    | Reward                                    |
| ------- | ----------------------------------------- |
| Spam    | +1 (correct), -1 (wrong)                  |
| Routing | +1 (correct), -0.5 (wrong)                |
| Reply   | Based on relevance, tone, and helpfulness |

Reward shaping ensures partial correctness is also encouraged.

---

## 🔌 API Endpoints

| Endpoint   | Description                        |
| ---------- | ---------------------------------- |
| GET /reset | Returns a new email                |
| POST /step | Takes an action and returns reward |
| GET /state | Returns current environment state  |

---

## 🤖 Agent (inference.py)

A rule-based agent is implemented to simulate intelligent decision-making across tasks.

---

## 🏗️ Architecture

* FastAPI-based backend
* Modular environment design (`env.py`, `grader.py`, `tasks.py`)
* Dockerized deployment
* Stateless API interaction

---

## 📊 Key Features

* Multi-task environment
* Realistic dataset (15+ emails)
* Reward shaping mechanism
* Error-safe API
* Clean reproducible outputs

---

## ▶️ How to Run

```bash
docker build -t email-env .
docker run -p 7860:7860 email-env
```

Open:

```
http://localhost:7860
```

---

## 🧪 Example Flow

1. Call `/reset` → receive email
2. Send action to `/step`
3. Receive reward and feedback

---

## 🔮 Future Scope

* LLM-based reply generation
* Multi-step conversations
* Analytics dashboard

---

## 👨‍💻 Author

Annanya Bagga
Sohini Dutta