
# 🚀 AutoStream Conversational AI Agent  
### (Social-to-Lead Agentic Workflow)

## 📌 Overview
This project implements a **Conversational AI Agent** for *AutoStream*, a fictional SaaS platform offering automated video editing tools.

The agent is designed to simulate a **real-world lead generation workflow**, where it:
- Understands user intent  
- Retrieves accurate product information using RAG  
- Identifies high-intent users  
- Captures leads via controlled tool execution  

---

## 🎯 Key Features

### 🔹 Intent Detection
The agent classifies user queries into:
- Greeting  
- Product/Pricing Inquiry  
- High-Intent Lead  

---

### 🔹 RAG (Retrieval-Augmented Generation)
- Uses a **local knowledge base (JSON)**  
- Retrieves:
  - Pricing details  
  - Product features  
  - Company policies  
- Ensures accurate and consistent responses  

---

### 🔹 Multi-Turn Conversation Management
- Maintains conversation state across multiple steps  
- Guides the user through a structured interaction flow  

---

### 🔹 Lead Capture Tool (Controlled Execution)
The agent collects:
- Name  
- Email  
- Platform (YouTube, Instagram, etc.)

⚠️ The lead capture function is triggered **only after all required details are collected**, ensuring proper workflow control.

---

## 🏗️ Architecture

This project follows a **LangGraph-inspired agent design pattern**:

- **State Management**  
  A custom `AgentState` class tracks:
  - Current conversation stage  
  - User-provided details  

- **Intent Classification Layer**  
  A modular classifier (`llm_intent_classifier`) determines user intent.  
  Designed to be easily replaceable with a real LLM (e.g., GPT-4o-mini).

- **RAG Layer**  
  Retrieves structured responses from a local JSON knowledge base.

- **Tool Execution Layer**  
  Executes `mock_lead_capture()` only after validation of collected inputs.

---

## 🔄 Conversation Workflow

1. User initiates conversation (Greeting)  
2. Agent responds and handles pricing queries (RAG)  
3. User shows interest in product (Intent Shift)  
4. Agent collects user details step-by-step  
5. Lead capture tool is executed  

---

## ⚙️ Tech Stack

- **Language:** Python 3.9+  
- **Framework:** LangGraph-inspired workflow (state-based design)  
- **LLM:** Simulated (can be replaced with GPT-4o-mini / Gemini / Claude)  
- **Data Storage:** Local JSON (knowledge base)  

---

## ▶️ How to Run Locally

### 1. Clone or Download the Repository
```bash
git clone <your-repo-link>
cd autostream-agent
