from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGODB_URI

client = AsyncIOMotorClient(MONGODB_URI)
db = client.fastapi # 'fastapi' es el nombre de la base de datos en MongoDB
note_collection = db.get_collection('notes')