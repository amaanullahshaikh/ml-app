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

```
ollama pull deepseek-r1:1.5b
```
# or
```
ollama pull llama3
```
# 3. 🛢️ PostgreSQL + pgvector Setup
Launch psql and run:
-- Enable vector extension
```
CREATE EXTENSION IF NOT EXISTS vector;
```

-- Create the database and user
```
CREATE DATABASE ragapp;
CREATE USER user_name WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE ragapp TO user_name;
```
No need to create tables manually. The app will auto-generate embedding tables.

# 4. ⚙️ Configure application.properties
```
spring.datasource.url=jdbc:postgresql://localhost:5432/ragapp
spring.datasource.username=your_userName
spring.datasource.password=password
spring.datasource.driver-class-name=org.postgresql.Driver

langchain4j.ollama.chat-model.timeout=180s
langchain4j.ollama.embedding-model.timeout=180s

logging.level.dev.langchain4j=DEBUG
logging.level.okhttp3=DEBUG
logging.level.com.ragApp=DEBUG
```
# 5. 🚀 Run the Application
```
mvn spring-boot:run
```
Then, open your browser:
http://localhost:8080

# 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.
