# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # from datetime import datetime
# # from typing import List

# # from .db import collection

# # # FastAPI app
# # app = FastAPI()

# # # Topic model (Pydantic)
# # class Topic(BaseModel):
# #     name: str
# #     added_at: datetime
# #     difficulty: int  # 1 = easy, 5 = hard
# #     priority: str  # "low", "medium", "high"

# # @app.get("/")
# # def home():
# #     return {"message": "Smart Study Scheduler backend is running!"}

# # # Endpoint to add a topic
# # @app.post("/topics")
# # async def add_topic(topic: Topic):
# #     topic_dict = topic.dict()
# #     topic_dict["added_at"] = topic.added_at.isoformat()  # Convert datetime to string for storage
# #     result = await collection.insert_one(topic_dict)  # Insert into MongoDB
# #     return {"message": "Topic added successfully", "topic_id": str(result.inserted_id)}

# # # Endpoint to fetch topics
# # @app.get("/topics", response_model=List[Topic])
# # async def get_topics():
# #     topics_cursor = collection.find()  # Fetch all topics from MongoDB
# #     topics_list = await topics_cursor.to_list(length=100)  # Get top 100 topics (or limit as per need)
# #     return topics_list



# # ********************************************************************************************************************************************8
# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # from datetime import datetime
# # from typing import List
# # from app.db import collection
# # from .db import collection  # Importing the collection from db.py

# # # FastAPI app
# # app = FastAPI()

# # async def create_dummy_document():
# #     # Check if the collection is empty
# #     count = await collection.count_documents({})
# #     if count == 0:
# #         # Insert a dummy topic if collection is empty
# #         await collection.insert_one({
# #             "name": "Dummy Topic",
# #             "added_at": datetime.utcnow().isoformat(),
# #             "difficulty": 3,
# #             "priority": "medium"
# #         })
        

# # # Topic model (Pydantic)
# # class Topic(BaseModel):
# #     name: str
# #     added_at: datetime
# #     difficulty: int  # 1 = easy, 5 = hard
# #     priority: str  # "low", "medium", "high"

# # @app.get("/")
# # def home():
# #     return {"message": "Smart Study Scheduler backend is running!"}

# # # Endpoint to add a topic
# # @app.post("/topics")
# # async def add_topic(topic: Topic):
# #     topic_dict = topic.dict()
# #     topic_dict["added_at"] = topic.added_at.isoformat()  # Convert datetime to string for storage
# #     result = await collection.insert_one(topic_dict)  # Insert into MongoDB collection
# #     return {"message": "Topic added successfully", "topic_id": str(result.inserted_id)}

# # # Endpoint to fetch topics
# # @app.get("/topics", response_model=List[Topic])
# # async def get_topics():
# #     topics_cursor = collection.find()  # Fetch all topics from MongoDB
# #     topics_list = await topics_cursor.to_list(length=100)  # Get top 100 topics
# #     return topics_list

# # from fastapi import FastAPI
# # from datetime import datetime
# # from typing import List

# # from app.db import collection  # MongoDB collection
# # from app.schemas import Topic  # Import Pydantic model

# # app = FastAPI()

# # @app.on_event("startup")
# # async def startup_event():
# #     # Ensure at least one document exists
# #     count = await collection.count_documents({})
# #     if count == 0:
# #         await collection.insert_one({
# #             "name": "Dummy Topic",
# #             "added_at": datetime.utcnow().isoformat(),
# #             "difficulty": 3,
# #             "priority": "medium"
# #         })

# # @app.get("/")
# # def home():
# #     return {"message": "Smart Study Scheduler backend is running!"}

# # @app.post("/topics")
# # async def add_topic(topic: Topic):
# #     topic_dict = topic.dict()
# #     topic_dict["added_at"] = topic.added_at.isoformat()  # Store datetime as ISO string
# #     result = await collection.insert_one(topic_dict)
# #     return {"message": "Topic added successfully", "topic_id": str(r
# # 
# # esult.inserted_id)}

# # @app.get("/topics", response_model=List[Topic])
# # async def get_topics():
# #     topics_cursor = collection.find()
# #     topics_list = await topics_cursor.to_list(length=100)
# #     return topics_list


# # from fastapi import FastAPI
# # from datetime import datetime
# # from typing import List
# # from motor.motor_asyncio import AsyncIOMotorClient
# # from app.schemas import Topic
# # #from app.db import topic_collection  # Assuming your db.py is set up correctly
# # from app.db import topic_collection, initialize 
# # app = FastAPI()

# # # Initialize the MongoDB client
# # @app.on_event("startup")
# # async def startup_event():
# #     # Ensure MongoDB connection is initialized first
# #     await initialize()

# #     # Ensure at least one document exists in the 'topic' collection
# #     count = await topic_collection.count_documents({})
# #     if count == 0:
# #         await topic_collection.insert_one({
# #             "name": "Dummy Topic",
# #             "added_at": datetime.utcnow().isoformat(),
# #             "difficulty": 3,
# #             "priority": "medium"
# #         })

# # @app.get("/")
# # def home():
# #     return {"message": "Smart Study Scheduler backend is running!"}

# # @app.post("/topics")
# # async def add_topic(topic: Topic):
# #     topic_dict = topic.dict()
# #     topic_dict["added_at"] = topic.added_at.isoformat()  # Store datetime as ISO string
# #     result = await topic_collection.insert_one(topic_dict)
# #     return {"message": "Topic added successfully", "topic_id": str(result.inserted_id)}

# # @app.get("/topics", response_model=List[Topic])
# # async def get_topics():
# #     topics_cursor = topic_collection.find()
# #     topics_list = await topics_cursor.to_list(length=100)
# #     return topics_list

# # from fastapi import FastAPI
# # from datetime import datetime
# # from typing import List
# # from app.schemas import Topic
# # from app.db import topic_collection, initialize  # Import MongoDB connection and initialization function

# # app = FastAPI()

# # # Initialize MongoDB connection on startup
# # @app.on_event("startup")
# # async def startup_event():
# #     await initialize()

# #     # Ensure at least one document exists in the 'topic' collection
# #     count = await topic_collection.count_documents({})
# #     if count == 0:
# #         await topic_collection.insert_one({
# #             "name": "Dummy Topic",
# #             "added_at": datetime.utcnow().isoformat(),
# #             "difficulty": 3,
# #             "priority": "medium"
# #         })

# # @app.get("/")
# # def home():
# #     return {"message": "Smart Study Scheduler backend is running!"}

# # @app.post("/topics")
# # async def add_topic(topic: Topic):
# #     topic_dict = topic.dict()
# #     topic_dict["added_at"] = topic.added_at.isoformat()  # Store datetime as ISO string
# #     result = await topic_collection.insert_one(topic_dict)
# #     return {"message": "Topic added successfully", "topic_id": str(result.inserted_id)}

# # @app.get("/topics", response_model=List[Topic])
# # async def get_topics():
# #     topics_cursor = topic_collection.find()
# #     topics_list = await topics_cursor.to_list(length=100)
# #     return topics_list

# from fastapi import FastAPI
# from datetime import datetime
# from typing import List
# from app.schemas import Topic
# from app.db import topic_collection, initialize  # Import MongoDB connection and initialization function

# app = FastAPI()

# # Initialize MongoDB connection on startup
# @app.on_event("startup")
# async def startup_event():
#     print("Attempting to connect to MongoDB...")
#     await initialize()
#     print("MongoDB connection established.")

#     # Ensure at least one document exists in the 'topic' collection
#     count = await topic_collection.count_documents({})
#     if count == 0:
#         print("No topics found, inserting a dummy topic.")
#         await topic_collection.insert_one({
#             "name": "Dummy Topic",
#             "added_at": datetime.utcnow().isoformat(),
#             "difficulty": 3,
#             "priority": "medium"
#         })
#     else:
#         print(f"Found {count} topics in the database.")

# @app.get("/")
# def home():
#     return {"message": "Smart Study Scheduler backend is running!"}

# @app.post("/topics")
# async def add_topic(topic: Topic):
#     print("Adding a new topic to the database.")
#     topic_dict = topic.dict()
#     topic_dict["added_at"] = topic.added_at.isoformat()  # Store datetime as ISO string
#     result = await topic_collection.insert_one(topic_dict)
#     print(f"Topic added with ID: {result.inserted_id}")
#     return {"message": "Topic added successfully", "topic_id": str(result.inserted_id)}

# @app.get("/topics", response_model=List[Topic])
# async def get_topics():
#     print("Fetching topics from the database.")
#     topics_cursor = topic_collection.find()
#     topics_list = await topics_cursor.to_list(length=100)
#     return topics_list


from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import List
from app.schemas import Topic
from app.db import topic_collection, initialize

app = FastAPI()

origins = [
    "http://localhost:8080",  # Or the origin of your Vue.js app (check in browser)
    "http://localhost:3000",  # Common port for Vue.js
    "http://127.0.0.1:8000", #if running on the same port
    "*", #BE VERY CAREFUL IN PRODUCTION
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def startup_event():
    print("Attempting to connect to MongoDB...")
    await initialize()
    print("MongoDB connection established.")

    count = await topic_collection.count_documents({})
    if count == 0:
        print("No topics found, inserting a dummy topic.")
        await topic_collection.insert_one({
            "name": "Dummy Topic",
            "added_at": datetime.utcnow(),  # Use datetime object here
            "difficulty": 3,
            "priority": "medium"
        })
    else:
        print(f"Found {count} topics in the database.")

@app.get("/")
def home():
    return {"message": "Smart Study Scheduler backend is running!"}

@app.post("/topics")
async def add_topic(topic: Topic):
    print("Adding a new topic to the database.")
    try:

        topic_dict = topic.dict()  # Get the dictionary representation
        result = await topic_collection.insert_one(topic_dict)
        print(f"Topic added with ID: {result.inserted_id}")
        return {"message": "Topic added successfully", "topic_id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding topic: {e}")


@app.get("/topics", response_model=List[Topic])
async def get_topics():
    print("Fetching topics from the database.")
    try:
        topics_cursor = topic_collection.find()
        topics_list = await topics_cursor.to_list(length=100)
        processed_topics = []
        for topic_data in topics_list:
            # Handle missing added_at
            added_at = topic_data.get("added_at")
            if not added_at:
                added_at = datetime.utcnow()
            elif isinstance(added_at, dict) and "$date" in added_at:
                added_at = datetime.fromtimestamp(added_at["$date"] / 1000)
            elif isinstance(added_at, str):
                added_at = datetime.fromisoformat(added_at.replace('Z', '+00:00')) # Handle potential Z timezone

            # Handle difficulty as string
            difficulty_str = topic_data.get("difficulty")
            difficulty = 3  # Default
            if isinstance(difficulty_str, str):
                if difficulty_str.lower() == "easy":
                    difficulty = 1
                elif difficulty_str.lower() == "medium":
                    difficulty = 3
                elif difficulty_str.lower() == "hard":
                    difficulty = 5
                else:
                    try:
                        difficulty = int(difficulty_str)
                    except ValueError:
                        pass # Keep default

            elif isinstance(difficulty_str, int):
                difficulty = difficulty_str

            # Handle missing priority
            priority = topic_data.get("priority", "medium")
            if isinstance(priority, int):
                if priority == 1:
                    priority = "low"
                elif priority == 3:
                    priority = "medium"
                elif priority == 5 or priority == 4: # Assuming 4 also maps to medium/high
                    priority = "high"
                else:
                    priority = str(priority) # Convert to string if unexpected int

            processed_topics.append(Topic(
                name=topic_data.get("name", ""),
                added_at=added_at,
                difficulty=difficulty,
                priority=priority
            ))
        print("About to return processed topics:", processed_topics)
        return processed_topics
    except Exception as e:
        print(f"Error fetching topics: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching topics: {e}")