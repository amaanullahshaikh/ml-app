# 🧠 RAG-Based Chatbot (Spring Boot + LangChain4j + Ollama + pgvector)

This project implements a **Retrieval-Augmented Generation (RAG)** based chatbot using **Spring Boot**, **LangChain4j**, **Ollama**, and **pgvector (PostgreSQL extension)**. It allows users to upload PDF documents and ask intelligent, context-aware questions powered by local LLMs.

---

## 🚀 Features

- 📁 Upload PDF documents
- 🧠 Document segmentation, vectorization, and storage using LangChain4j
- 🗃️ Embeddings stored in **PostgreSQL** with **pgvector**
- 🤖 Context-aware answers via **Ollama LLMs** (e.g., DeepSeek, LLaMA3)
- 🔄 Streaming responses (real-time feedback)
- ⚡ Fully offline and privacy-respecting
- 🎨 Simple web frontend using HTML + Tailwind CSS

---

## 🛠️ Tech Stack

| Layer         | Technology                         |
|---------------|-------------------------------------|
| **Backend**   | Spring Boot                         |
| **LLM**       | Ollama (e.g., deepseek-r1:1.5b)     |
| **RAG Engine**| LangChain4j                         |
| **Embeddings**| OllamaEmbeddingModel                |
| **Vector DB** | PostgreSQL + pgvector               |
| **Frontend**  | HTML + Tailwind CSS + JavaScript    |
| **Build Tool**| Maven                               |

---

## ⚙️ Installation & Setup

### 1. 📦 Prerequisites

- Java 17+
- Maven
- PostgreSQL 15+ with `pgvector`
- [Ollama](https://ollama.com) installed and running locally
- Git (for version control)

---

### 2. 📥 Pull Ollama Model

You must pull the language model you'd like to use with Ollama:

```bash
ollama pull deepseek-r1:1.5b
# or
ollama pull llama3

-- Enable vector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create the database and user
CREATE DATABASE ragapp;
CREATE USER amanulla WITH PASSWORD 'aman1234';
GRANT ALL PRIVILEGES ON DATABASE ragapp TO amanulla;

spring.application.name=RAG Chatbot
server.port=8080

# Ollama model
ollama.model=deepseek-r1:1.5b
ollama.base-url=http://localhost:11434

mvn spring-boot:run

Then, open your browser:
http://localhost:8080
