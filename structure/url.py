import os
from motor.motor_asyncio import AsyncIOMotorClient


# Read the MongoDB URI from the environment variable
MONGODB_URI = os.getenv("mongo_url")

client = AsyncIOMotorClient(MONGODB_URI)

db = client.flowers

#iris_test is the name of the collection in which flower parameters are stored
iris_test = db.iris_testing
