from celery import Celery

celery_app = Celery(
    "chunking_pipeline",
    backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0"
)

@celery_app.task
def chunk_text_task(text: str, chunk_size: int, task_id: str):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return {"task_id": task_id, "chunks": chunks}
