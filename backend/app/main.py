from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List
from .routes import study
app = FastAPI()

# Temporary in-memory list to store topics
topics = []
app.include_router(study.router)
# Topic model
class Topic(BaseModel):
    name: str
    added_at: datetime
    difficulty: int  # 1 = easy, 5 = hard
    priority: str  # "low", "medium", "high"

@app.get("/")
def home():
    return {"message": "Smart Study Scheduler backend is running!"}

@app.post("/topics")
def add_topic(topic: Topic):
    topics.append(topic)
    return {"message": "Topic added successfully", "topic": topic}

@app.get("/topics")
def get_topics():
    return topics
