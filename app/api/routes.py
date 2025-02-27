from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from app.workers.tasks import chunk_text_task
import uuid

router = APIRouter()

class ChunkRequest(BaseModel):
    text: str
    chunk_size: int

@router.post("/chunk/")
async def chunk_text(request: ChunkRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    background_tasks.add_task(chunk_text_task, request.text, request.chunk_size, task_id)
    return {"task_id": task_id, "status": "Processing"}
