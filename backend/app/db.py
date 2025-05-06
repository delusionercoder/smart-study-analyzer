from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# MongoDB URI
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

# Access the database
db = client["smartStudyAnalyzer"]

# Access the 'topic' collection
topic_collection = db["topic"]

# Function to initialize connection (can include additional setup if needed)
async def initialize():
    try:
        print("Attempting to connect to MongoDB...")
        await client.admin.command('ping')
        print("MongoDB connection established.")
    except Exception as e:
        print("Error while connecting to MongoDB:", e)
        raise e
