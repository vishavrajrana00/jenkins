# # main.py
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# from typing import List, Optional
# from motor.motor_asyncio import AsyncIOMotorClient
# from bson import ObjectId
# import os

# print("=============")
# # ---------- Config ----------
# MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://admin:adminpassword@localhost:27017")
# DB_NAME = os.getenv("MONGODB_DB", "sampledb")
# COLLECTION_NAME = os.getenv("MONGODB_COLLECTION", "records")

# # ---------- App & DB client ----------
# app = FastAPI(title="Simple FastAPI + MongoDB example")

# mongo_client = AsyncIOMotorClient(MONGODB_URI)
# db = mongo_client[DB_NAME]
# collection = db[COLLECTION_NAME]

# # ---------- Helpers ----------
# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid objectid")
#         return ObjectId(v)

# def doc_to_dict(doc):
#     """Convert MongoDB document to JSON-serializable dict."""
#     if not doc:
#         return None
#     d = {k: v for k, v in doc.items() if k != "_id"}
#     d["id"] = str(doc["_id"])
#     return d

# # ---------- Pydantic models ----------
# class RecordIn(BaseModel):
#     title: str = Field(..., example="Sample title")
#     description: Optional[str] = Field(None, example="Optional description")
#     tags: Optional[List[str]] = Field(default_factory=list)

# class RecordOut(RecordIn):
#     id: str

# # ---------- Routes ----------
# @app.get("/records", response_model=List[RecordOut])
# async def list_records(limit: int = 50, skip: int = 0):
#     """
#     List records. Optional query params:
#     - limit: max number of records (default 50)
#     - skip: number to skip (default 0)
#     """
#     cursor = collection.find().skip(skip).limit(limit)
#     docs = []
#     async for doc in cursor:
#         docs.append(doc_to_dict(doc))
#     return docs

# @app.post("/records", response_model=RecordOut, status_code=201)
# async def create_record(record: RecordIn):
#     """
#     Insert a new record and return it including generated id.
#     """
#     data = record.dict()
#     result = await collection.insert_one(data)
#     created = await collection.find_one({"_id": result.inserted_id})
#     if not created:
#         raise HTTPException(status_code=500, detail="Failed to retrieve created record")
#     return doc_to_dict(created)

# # Optional health check
# @app.get("/health")
# async def health():
#     try:
#         # ping the server
#         await mongo_client.admin.command("ping")
#         return {"status": "ok"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"db ping failed: {e}")




from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Dynamic endpoint with a path parameter
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
