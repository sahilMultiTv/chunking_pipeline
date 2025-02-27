# 🚀 Chunking Pipeline

## 📌 Overview
The **Chunking Pipeline** is a scalable and modular service built using **FastAPI, Celery, Redis, and PostgreSQL**. It supports efficient data chunking and processing using an asynchronous task queue.

---

## 🔧 Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone git@github.com:sahilMultiTv/chunking_pipeline.git
cd chunking-pipeline
```

### **2️⃣ Configure Environment Variables**
Modify the `.env` file as needed.
```ini
DATABASE_URL=postgresql://user:password@localhost/chunking_db
REDIS_URL=redis://localhost:6379/0
```

---

## 🌍 Running in Development Mode (Hot Reload Enabled)
💡 Development mode allows **real-time updates** without restarting the server.

### **🔹 Start Backend (FastAPI)**
1. **Activate Virtual Environment**
   ```bash
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows (PowerShell)
   ```
2. **Start FastAPI with Auto-Reload**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```
3. **Start Celery Worker**
   ```bash
   celery -A app.workers.tasks worker --loglevel=info --concurrency=4
   ```
4. **Start Redis (If Not Running)**
   ```bash
   redis-server
   ```
5. **Start PostgreSQL (If Not Running)**
   ```bash
   sudo service postgresql start  # Linux/Mac
   ```

---

## 🐳 Running in Docker Mode
💡 This mode starts all services (**FastAPI, Celery, Redis, PostgreSQL**) in **containers**.

### **🔹 Start Services**
   ```bash
   docker-compose up --build
   ```

### **🔹 Stop Services**
   ```bash
   docker-compose down
   ```

---

## 🚀 Access API
- **Swagger UI** → [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc API Docs** → [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🛠️ Test API
1. **Using cURL**
   ```bash
   curl -X POST "http://localhost:8000/chunk/" -H "Content-Type: application/json" -d '{"text": "Hello, this is a test.", "chunk_size": 5}'
   ```
2. **Using Postman or Browser**
   - Open [http://localhost:8000/docs](http://localhost:8000/docs)
   - Try the `/chunk/` endpoint.

---

## 📌 Deployment Guide

### **1️⃣ Deploy Using Docker**
💡 Ensure Docker is installed and configured.

1. **Build and Run the Containers**
   ```bash
   docker-compose up --build -d
   ```
2. **Check Running Containers**
   ```bash
   docker ps
   ```
3. **Stop Services**
   ```bash
   docker-compose down
   ```

### **2️⃣ Deploy to Cloud (AWS, GCP, or Azure)**

- **Using AWS ECS (Elastic Container Service)**:
  - Build and push the image to **Amazon ECR**.
  - Deploy using **ECS + Fargate**.
- **Using Kubernetes**:
  - Deploy using **Helm Charts** or **Kubernetes YAML files**.
- **Using Heroku**:
  - Deploy via **Docker** or **Heroku CLI**.

---

## 📌 Choosing the Right Mode
| Mode             | Command                                        | Notes |
|----------------|-----------------------------------------------|-------|
| **Development** | `uvicorn app.main:app --reload`             | Auto-reloads on changes |
| **Celery Worker** | `celery -A app.workers.tasks worker --loglevel=info` | Async processing |
| **Docker Mode** | `docker-compose up --build`                  | Runs all services |
| **Stop Services** | `docker-compose down`                        | Stops everything |

---

## ✅ Next Steps
- [ ] **Integrate NLP-based chunking**
- [ ] **Add WebSocket for real-time chunking updates**
- [ ] **Deploy to Kubernetes**

Let me know if you need any modifications or additional configurations! 🚀🔥

