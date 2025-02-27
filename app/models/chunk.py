from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Chunk(Base):
    __tablename__ = "chunks"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(String, index=True)
    chunk = Column(String)
