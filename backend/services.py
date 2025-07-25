from mock_data import get_mock_courses

def search_courses(query: str):
    courses = get_mock_courses()
    return [c for c in courses if query.lower() in c.name.lower() or query.lower() in c.location.lower()]


# main.py
from fastapi import FastAPI, Query
from schemas import Course
from config import add_cors
from services import search_courses
from typing import List

app = FastAPI()
add_cors(app)

@app.get("/api/search", response_model=List[Course])
async def search(query: str = Query(..., min_length=3)):
    return search_courses(query)