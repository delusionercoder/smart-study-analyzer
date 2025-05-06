# from pydantic import BaseModel
# from datetime import datetime

# class StudySessionCreate(BaseModel):
#     user_id: int
#     topic: str
#     duration: float

# class StudySessionOut(BaseModel):
#     id: int
#     topic: str
#     duration: float
#     timestamp: datetime

#     class Config:
#         orm_mode = True
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

class Topic(BaseModel):
    name: str
    added_at: datetime
    difficulty: int  # 1 = easy, 5 = hard
    priority: str  # "low", "medium", "high"
