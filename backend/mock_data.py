from datetime import datetime, timedelta
from schemas import Course, TeeTime

def get_mock_courses():
    now = datetime.now()
    soon = (now + timedelta(minutes=30)).strftime("%I:%M %p")
    return [
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