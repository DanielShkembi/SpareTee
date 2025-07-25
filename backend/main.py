from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime, timedelta

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class TeeTime(BaseModel):
    id: int
    time: str
    discountedPrice: float

class Course(BaseModel):
    id: int
    name: str
    location: str
    availableTeeTimes: List[TeeTime]

@app.get("/")
def read_root():
    return {"message": "SpareTee API is working"}

@app.get("/api/search", response_model=List[Course])
async def search_courses(query: str = Query(..., min_length=3)):
    now = datetime.now()
    soon = (now + timedelta(minutes=30)).strftime("%I:%M %p")

    demo = [
        Course(
            id=1,
            name="Lincoln Park Golf Course",
            location="Chicago, IL",
            availableTeeTimes=[
                TeeTime(id=101, time=soon, discountedPrice=29.99),
                TeeTime(id=102, time="12:10 PM", discountedPrice=34.99),
            ]
        ),
        Course(
            id=2,
            name="Cog Hill Golf & Country Club",
            location="Lemont, IL",
            availableTeeTimes=[],
        ),
    ]
    return [c for c in demo if query.lower() in c.name.lower() or query.lower() in c.location.lower()]
