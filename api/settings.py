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

VERSION = (3, 0, 0)


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
        },
        {
            "name": "Basic Route"
        },
    ],
    "version": "".join(map(str, VERSION)),
    "description": DESCRIPTION,
    "redoc_url": None,
    "docs_url": '/'
}


__all__ = ["FASTAPI_SETTINGS", "DATABASE_SETTINGS", ]