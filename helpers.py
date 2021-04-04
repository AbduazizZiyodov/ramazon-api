from datetime import date
from fastapi import FastAPI
from fastapi import HTTPException
from tortoise.contrib.fastapi import register_tortoise



current = date.today().strftime("%Y-%m-%d")


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
