from pydantic import BaseModel
from typing import List

class TeeTime(BaseModel):
    id: int
    time: str
    discountedPrice: float

class Course(BaseModel):
    id: int
    name: str
    location: str
    availableTeeTimes: List[TeeTime]