from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

from .db import collection

# FastAPI app
app = FastAPI()

# Topic model (Pydantic)
class Topic(BaseModel):
    name: str
    added_at: datetime
    difficulty: int  # 1 = easy, 5 = hard
    priority: str  # "low", "medium", "high"

@app.get("/")
def home():
    return {"message": "Smart Study Scheduler backend is running!"}

# Endpoint to add a topic
@app.post("/topics")
async def add_topic(topic: Topic):
    topic_dict = topic.dict()
    topic_dict["added_at"] = topic.added_at.isoformat()  # Convert datetime to string for storage
    result = await collection.insert_one(topic_dict)  # Insert into MongoDB
    return {"message": "Topic added successfully", "topic_id": str(result.inserted_id)}

# Endpoint to fetch topics
@app.get("/topics", response_model=List[Topic])
async def get_topics():
    topics_cursor = collection.find()  # Fetch all topics from MongoDB
    topics_list = await topics_cursor.to_list(length=100)  # Get top 100 topics (or limit as per need)
    return topics_list
