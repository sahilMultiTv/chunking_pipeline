# 🚀 Chunking Pipeline

## 🔧 Setup & Run

1. **Run the script:**
   ```bash
   bash setup_chunking_pipeline.sh
   ```

2. **Start services:**
   ```bash
   docker-compose up --build
   ```

3. **Access API at:** 

4. **Test API:**
   ```bash
   curl -X POST "http://localhost:8000/chunk/" -H "Content-Type: application/json" -d '{"text": "Hello, this is a test.", "chunk_size": 5}'
   ```
