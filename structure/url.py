import os
from motor.motor_asyncio import AsyncIOMotorClient


# Read the MongoDB URI from the environment variable
MONGODB_URI = 'mongodb+srv://jeankirstein6104:UaSXsPMMz99Acj9v@basics-projects.buat5ge.mongodb.net/?retryWrites=true&w=majority&appName=basics-projects'

client = AsyncIOMotorClient(MONGODB_URI)

db = client.flowers

#iris_test is the name of the collection in which flower parameters are stored
iris_test = db.iris_testing
