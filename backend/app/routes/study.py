from fastapi import APIRouter, HTTPException
from ..db import study_collection
from ..models import StudySession
from datetime import datetime

router = APIRouter(prefix="/study", tags=["Study Sessions"])

@router.post("/")
async def create_session(session: StudySession):
    session_dict = session.dict()
    session_dict["timestamp"] = datetime.utcnow()
    result = await study_collection.insert_one(session_dict)
    return {"id": str(result.inserted_id), **session_dict}

@router.get("/{user_id}")
async def get_sessions(user_id: str):
    sessions = await study_collection.find({"user_id": user_id}).to_list(100)
    return sessions
