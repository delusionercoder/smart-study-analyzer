from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"  # or your Atlas URI

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.study_scheduler

study_collection = database.get_collection("study_sessions")
