from pydantic import BaseModel
from datetime import datetime

class StudySessionCreate(BaseModel):
    user_id: int
    topic: str
    duration: float

class StudySessionOut(BaseModel):
    id: int
    topic: str
    duration: float
    timestamp: datetime

    class Config:
        orm_mode = True
