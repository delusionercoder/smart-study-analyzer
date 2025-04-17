from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB URI and database setup
MONGO_URI = "mongodb://localhost:27017"  # Replace with your Compass URI if using cloud MongoDB
DB_NAME = "smartStudyAnalyzer"
COLLECTION_NAME = "topics"  # You can change this to match the correct collection name

# Create an AsyncIOMotorClient instance and access the database and collection
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
