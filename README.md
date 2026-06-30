# 🤖 AI HR Support Agent

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![LangChain](https://img.shields.io/badge/LangChain-RAG-brightgreen)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-red)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow)
![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-all--MiniLM--L6--v2-orange)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![HTML](https://img.shields.io/badge/HTML-Frontend-orange)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-UI-38B2AC)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E)
![RAG](https://img.shields.io/badge/RAG-Enabled-success)
![Self Learning](https://img.shields.io/badge/Self--Learning-Enabled-purple)

An intelligent HR Support Assistant built using **FastAPI**, **LangChain**, **FAISS**, and **Hugging Face Embeddings**. The application answers HR policy questions, creates IT support tickets, and continuously improves through a self-learning knowledge base.

---

## 🚀 Features

* 📄 HR Policy Question Answering
* 🧠 Retrieval-Augmented Generation (RAG) using FAISS
* 📚 Upload HR policy documents (PDF/TXT/MD)
* 💾 Self-learning memory for new questions and answers
* 🎫 Automatic IT support ticket creation
* 🔍 Semantic search using Hugging Face embeddings
* 🌐 FastAPI backend with responsive web interface
* ⚡ Lightweight and easy to extend

---

## 🛠 Tech Stack

### Backend

* FastAPI
* Uvicorn
* SQLAlchemy
* SQLite

### AI & NLP

* LangChain
* FAISS
* HuggingFace Embeddings
* Sentence Transformers

### Frontend

* HTML
* Tailwind CSS
* JavaScript

### Database

* SQLite

---

## 📂 Project Structure

```text
AI-HR-Support-Agent/
│
├── main.py
├── database.py
├── requirements.txt
│
├── routers/
│   ├── agent.py
│   ├── auth.py
│   └── documents.py
│
├── services/
│   ├── agent_service.py
│   └── rag_service.py
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── faiss_index/
│
├── memory_index/
│
├── models/
│
├── utils/
│
└── static/
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-HR-Support-Agent.git

cd AI-HR-Support-Agent
```

---

### 2. Create Virtual Environment

```bash
conda create -n hragent python=3.11

conda activate hragent
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Start Server

```bash
uvicorn main:app --reload
```

---

### 5. Open Browser

```
http://127.0.0.1:8000
```

---

## 📤 Upload HR Documents

Supported formats

* PDF
* TXT
* Markdown

Upload endpoint

```
POST /documents/upload
```

Uploaded documents are automatically:

* Parsed
* Split into chunks
* Converted into embeddings
* Stored in the FAISS vector database

---

## 💬 Sample Questions

### HR Policies

* What is the leave policy?
* How many sick leaves are available?
* How many earned leaves do employees receive?
* Can unused earned leaves be carried forward?
* What is the notice period?
* Can the notice period be reduced?
* What are the office timings?
* What employee benefits are available?
* Do employees get provident fund benefits?
* Can I work remotely?
* What is the work from home policy?
* What is the travel reimbursement policy?

---

### IT Support

* My laptop is broken.
* Printer is not working.
* WiFi is not working.
* VPN is not working.
* Network connection issue.
* Email is not working.
* I need software installation.

The system automatically creates an IT support ticket.

Example

```
🎟 Support Ticket Created

Ticket ID: IT-4821

Issue: Printer is not working.

Status: Open
```

---

## 🧠 Self Learning

The agent supports incremental learning.

New knowledge can be added using

```
POST /agent/learn
```

Example

Question

```
What is the dress code?
```

Answer

```
Employees are expected to wear business casual attire.
```

Future queries will retrieve the learned answer automatically.

---

## 🔄 Application Workflow

```
User Question
      │
      ▼
FastAPI API
      │
      ▼
Agent Service
      │
      ▼
───────────────
│ Memory Search │
───────────────
      │
      ▼
───────────────
│ FAISS Search  │
───────────────
      │
      ▼
Generate Response
      │
      ▼
Return Answer

OR

Create IT Support Ticket
```

---

## 📸 Screenshots

Add screenshots here.

### Home Page

```
images/home.png
```

### HR Question Answering

```
images/hr_query.png
```

### IT Ticket Creation

```
images/ticket.png
```

---

## 🔮 Future Improvements

* Integration with Large Language Models (LLMs)
* JWT Authentication
* Role-based access control
* Email notifications
* Employee portal integration
* Multi-document knowledge base
* Chat history
* Voice-based HR assistant
* Dashboard and analytics

---

## 👩‍💻 Author

**Shreya Sidabache**
---


