from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class StudySession(BaseModel):
    user_id: str
    topic: str
    duration: float
    timestamp: Optional[datetime] = None
