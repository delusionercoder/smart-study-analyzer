
# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from datetime import datetime
# from typing import List
# from app.schemas import Topic
# from app.db import topic_collection, initialize

# app = FastAPI()

# origins = [
#     "http://localhost:8080",  # Or the origin of your Vue.js app (check in browser)
#     "http://localhost:3000",  # Common port for Vue.js
#     "http://127.0.0.1:8000", #if running on the same port
#     "*", #BE VERY CAREFUL IN PRODUCTION
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allows all headers
# )

# @app.on_event("startup")
# async def startup_event():
#     print("Attempting to connect to MongoDB...")
#     await initialize()
#     print("MongoDB connection established.")

#     count = await topic_collection.count_documents({})
#     if count == 0:
#         print("No topics found, inserting a dummy topic.")
#         await topic_collection.insert_one({
#             "name": "Dummy Topic",
#             "added_at": datetime.utcnow(),  # Use datetime object here
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
#     try:

#         topic_dict = topic.dict()  # Get the dictionary representation
#         result = await topic_collection.insert_one(topic_dict)
#         print(f"Topic added with ID: {result.inserted_id}")
#         return {"message": "Topic added successfully", "topic_id": str(result.inserted_id)}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error adding topic: {e}")


# @app.get("/topics", response_model=List[Topic])
# async def get_topics():
#     print("Fetching topics from the database.")
#     try:
#         topics_cursor = topic_collection.find()
#         topics_list = await topics_cursor.to_list(length=100)
#         processed_topics = []
#         for topic_data in topics_list:
#             # Handle missing added_at
#             added_at = topic_data.get("added_at")
#             if not added_at:
#                 added_at = datetime.utcnow()
#             elif isinstance(added_at, dict) and "$date" in added_at:
#                 added_at = datetime.fromtimestamp(added_at["$date"] / 1000)
#             elif isinstance(added_at, str):
#                 added_at = datetime.fromisoformat(added_at.replace('Z', '+00:00')) # Handle potential Z timezone

#             # Handle difficulty as string
#             difficulty_str = topic_data.get("difficulty")
#             difficulty = 3  # Default
#             if isinstance(difficulty_str, str):
#                 if difficulty_str.lower() == "easy":
#                     difficulty = 1
#                 elif difficulty_str.lower() == "medium":
#                     difficulty = 3
#                 elif difficulty_str.lower() == "hard":
#                     difficulty = 5
#                 else:
#                     try:
#                         difficulty = int(difficulty_str)
#                     except ValueError:
#                         pass # Keep default

#             elif isinstance(difficulty_str, int):
#                 difficulty = difficulty_str

#             # Handle missing priority
#             priority = topic_data.get("priority", "medium")
#             if isinstance(priority, int):
#                 if priority == 1:
#                     priority = "low"
#                 elif priority == 3:
#                     priority = "medium"
#                 elif priority == 5 or priority == 4: # Assuming 4 also maps to medium/high
#                     priority = "high"
#                 else:
#                     priority = str(priority) # Convert to string if unexpected int

#             processed_topics.append(Topic(
#                 name=topic_data.get("name", ""),
#                 added_at=added_at,
#                 difficulty=difficulty,
#                 priority=priority
#             ))
#         print("About to return processed topics:", processed_topics)
#         return processed_topics
#     except Exception as e:
#         print(f"Error fetching topics: {e}")
#         raise HTTPException(status_code=500, detail=f"Error fetching topics: {e}")

# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from datetime import datetime
# from typing import List, Dict
# from pydantic import BaseModel
# import re
# # Assuming your schemas.py and db.py are in the 'app' directory
# from app.schemas import Topic
# from app.db import topic_collection, initialize

# app = FastAPI()

# origins = [
#     "http://localhost:8080",
#     "http://localhost:3000",
#     "http://127.0.0.1:8000",
#     "*",  # Be cautious with this in production
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.on_event("startup")
# async def startup_event():
#     print("Attempting to connect to MongoDB...")
#     await initialize()
#     print("MongoDB connection established.")

#     count = await topic_collection.count_documents({})
#     if count == 0:
#         print("No topics found, inserting a dummy topic.")
#         await topic_collection.insert_one({
#             "name": "Dummy Topic",
#             "added_at": datetime.utcnow(),
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
#     try:
#         topic_dict = topic.dict()
#         result = await topic_collection.insert_one(topic_dict)
#         print(f"Topic added with ID: {result.inserted_id}")
#         return {"message": "Topic added successfully", "topic_id": str(result.inserted_id)}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error adding topic: {e}")


# @app.get("/topics", response_model=List[Topic])
# async def get_topics():
#     print("Fetching topics from the database.")
#     try:
#         topics_cursor = topic_collection.find()
#         topics_list = await topics_cursor.to_list(length=100)
#         processed_topics = []
#         for topic_data in topics_list:
#             # Handle missing added_at
#             added_at = topic_data.get("added_at")
#             if not added_at:
#                 added_at = datetime.utcnow()
#             elif isinstance(added_at, dict) and "$date" in added_at:
#                 added_at = datetime.fromtimestamp(added_at["$date"] / 1000)
#             elif isinstance(added_at, str):
#                 try:
#                     added_at = datetime.fromisoformat(added_at.replace('Z', '+00:00')) # Handle potential Z timezone
#                 except ValueError:
#                     added_at = datetime.utcnow() # Fallback if parsing fails

#             # Handle difficulty as string
#             difficulty_str = topic_data.get("difficulty")
#             difficulty = 3  # Default
#             if isinstance(difficulty_str, str):
#                 if difficulty_str.lower() == "easy":
#                     difficulty = 1
#                 elif difficulty_str.lower() == "medium":
#                     difficulty = 3
#                 elif difficulty_str.lower() == "hard":
#                     difficulty = 5
#                 else:
#                     try:
#                         difficulty = int(difficulty_str)
#                     except ValueError:
#                         pass # Keep default
#             elif isinstance(difficulty_str, int):
#                 difficulty = difficulty_str

#             # Handle missing priority
#             priority = topic_data.get("priority", "medium")
#             if isinstance(priority, int):
#                 if priority == 1:
#                     priority = "low"
#                 elif priority == 3:
#                     priority = "medium"
#                 elif priority == 5 or priority == 4: # Assuming 4 also maps to medium/high
#                     priority = "high"
#                 else:
#                     priority = str(priority) # Convert to string if unexpected int

#             processed_topics.append(Topic(
#                 name=topic_data.get("name", ""),
#                 added_at=added_at,
#                 difficulty=difficulty,
#                 priority=priority
#             ))
#         print("About to return processed topics:", processed_topics)
#         return processed_topics
#     except Exception as e:
#         print(f"Error fetching topics: {e}")
#         raise HTTPException(status_code=500, detail=f"Error fetching topics: {e}")


# class SyllabusInput(BaseModel):
#     syllabus_text: str

# class TopicStructure(BaseModel):
#     nodes: List[Dict] = []
#     edges: List[Dict] = []

# @app.post("/generate-syllabus-structure")
# async def generate_syllabus_structure(syllabus_input: SyllabusInput):
#     return {"message": "Endpoint is working"}

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime ,timedelta
from typing import List, Dict
from pydantic import BaseModel
import re
# Assuming your schemas.py and db.py are in the 'app' directory
from app.schemas import Topic
from app.db import topic_collection, initialize

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "*",  # Be cautious with this in production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
            "added_at": datetime.utcnow(),
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
        topic_dict = topic.dict()
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
                try:
                    added_at = datetime.fromisoformat(added_at.replace('Z', '+00:00')) # Handle potential Z timezone
                except ValueError:
                    added_at = datetime.utcnow() # Fallback if parsing fails

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


class OneDayPlanInput(BaseModel):
    subject: str
    topics: str  # comma or newline separated
    hours: float

@app.post("/generate-one-day-plan")
def generate_one_day_plan(input: OneDayPlanInput):
    try:
        topics_raw = re.split(r",|\n", input.topics)
        topics = [t.strip() for t in topics_raw if t.strip()]
        total_time = input.hours
        time_per_topic = round(total_time * 60 / len(topics))  # in minutes

        current_time = datetime.strptime("09:00", "%H:%M")
        plan = []
        pomodoro_cycle = 0

        for topic in topics:
            # Study period
            end_time = current_time + timedelta(minutes=time_per_topic)
            time_block = f"{current_time.strftime('%I:%M %p')} – {end_time.strftime('%I:%M %p')}"
            plan.append({
                "time": time_block,
                "topic": topic,
                "type": "study"
            })
            current_time = end_time
            pomodoro_cycle += 1

            # Break after each study period (Pomodoro method)
            if pomodoro_cycle % 4 == 0:
                break_time = current_time + timedelta(minutes=15)  # Long break after 4 cycles
                plan.append({
                    "time": f"{current_time.strftime('%I:%M %p')} – {break_time.strftime('%I:%M %p')}",
                    "topic": "Break (15 minutes)",
                    "type": "break"
                })
                current_time = break_time
            else:
                break_time = current_time + timedelta(minutes=5)  # Short break (5 minutes)
                plan.append({
                    "time": f"{current_time.strftime('%I:%M %p')} – {break_time.strftime('%I:%M %p')}",
                    "topic": "Break (5 minutes)",
                    "type": "break"
                })
                current_time = break_time

        return {"plan": plan}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")