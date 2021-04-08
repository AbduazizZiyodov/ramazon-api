import pytz
from datetime import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from tortoise.contrib.fastapi import register_tortoise


current = datetime.now(pytz.timezone('Asia/Tashkent')).strftime("%Y-%m-%d")

metadata = [
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
]


def configure_db(app: FastAPI):
    register_tortoise(
        app,
        db_url="sqlite://db.sqlite3",
        modules={'models': ['database.models']},
        generate_schemas=True,
        add_exception_handlers=True,
    )


def http_404():
    raise HTTPException(
        status_code=404, detail="Ma'lumot Topilmadi")
