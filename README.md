# Event-Driven Order Processing System

An event-driven backend system implemented in **Python** using **FastAPI**, demonstrating how real-world order processing systems handle **asynchronous workflows, retries, and failures**.

This project simulates how large-scale platforms (like Amazon) process orders using **events and background workers** instead of tightly coupled services.

---

## 📌 Problem Statement

In real e-commerce systems, placing an order should not block:
- Payment processing
- Inventory updates
- Notifications

Instead, systems publish events and allow independent services to react asynchronously.  
This project demonstrates that architecture in a simplified but realistic way.

---

## 🧠 System Architecture

The system is composed of three main components:

### 1️⃣ Order API (Producer)
- Accepts order requests
- Publishes `OrderPlaced` events to a queue
- Remains fast and responsive

### 2️⃣ Event Queue
- Acts as a message broker (in-memory)
- Decouples API from processing logic
- Supports retries and dead-letter handling

### 3️⃣ Worker (Consumer)
- Continuously listens for events
- Processes payment, inventory, and notification tasks
- Handles failures with retries and dead-letter queue

--- 
---

## ⚙️ Key Features

### ✅ Event-Driven Architecture
- Loose coupling between services
- Asynchronous processing
- Improved system scalability

### 🔁 Retry Mechanism
- Failed events are retried up to a fixed limit
- Retry count is tracked inside the event

### ☠️ Dead-Letter Queue (DLQ)
- Events that fail repeatedly are moved to a DLQ
- Prevents system crashes
- Enables failure isolation and debugging

### 💥 Failure Simulation
- Payment failures are randomly simulated
- Mimics real-world unreliable external services

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.10+
- pip

### Setup
```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install fastapi uvicorn


## 🔄 Event Flow
🧪 Observed Behavior

Orders are accepted instantly

Background worker processes events

Failures trigger retries

After max retries, events are sent to DLQ

🛠️ Tech Stack

Python

FastAPI

Uvicorn

In-memory queues

Asynchronous workers

🎯 Key Learnings

Designing event-driven systems

Decoupling APIs from business logic

Handling failures gracefully

Implementing retries and dead-letter queues

Thinking in terms of scalable backend systems

🔮 Future Improvements

Persistent message broker (Kafka/RabbitMQ)

Multiple worker instances

Database-backed order storage

Metrics and monitoring

📎 Author

Ishita Singh
GitHub: https://github.com/Butterfly132
