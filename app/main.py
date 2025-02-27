from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Chunking Pipeline")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Chunking Pipeline is running!"}
