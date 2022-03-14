import pytz
from datetime import (
    date,
    datetime,
    timedelta
)

TESTING: bool = True

TITLE: str = "RamadanAPI"

DESCRIPTION: str = """
**API** for Ramadan Calendar(2021). 
<br> Assalamu alaikum👋 Ramadan Mubarak. 
Wishing you a blessed and Happy Ramadan! 
<br> Data about times in this month is extremely important. 
<br> That's why I transferred this information to the **API** interface. 
This **API** will benefit everyone!
<br> **Author: Abduaziz Ziyodov**
"""


DATABASE_SETTINGS = {
    "db_url": "sqlite://api/database/database.sqlite",
    "modules": {
        'models': ['api.database.models']
    },
    "generate_schemas": True,
    "add_exception_handlers": True,
}

FASTAPI_SETTINGS = {
    "title": TITLE,
    "openapi_tags": [
        {
            "name": "Regions",
            "description": "Operations with regions"
        },
        {
            "name": "Dates",
            "description": "Operations with dates"
        }
    ],
    "version": "3.0.0",
    "description": DESCRIPTION,
    "redoc_url": None,
    "docs_url": '/swagger'
}

TIMEZONE = "Asia/Tashkent"


def get_current_time() -> date:
    """
    Returns current DateTime according to timezone
    """
    return datetime.now(pytz.timezone(TIMEZONE)).date()


MONTH: int = 30  # days

START_OF_RAMADAN: date = date(2022, 4, 2)
END_OF_RAMADAN: date = date(2022, 5, 2)

if TESTING:
    START_OF_RAMADAN: date = get_current_time()
    END_OF_RAMADAN: date = START_OF_RAMADAN + timedelta(days=MONTH)
