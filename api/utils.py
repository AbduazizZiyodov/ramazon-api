from fastapi import FastAPI
from datetime import timedelta
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from api import settings
from api.database.models import *

from api.settings import MONTH
from api.settings import START_OF_RAMADAN


def generate_days() -> dict:
    """
    Generates days for Ramadan.
    e.g First day of ramadan = 01.12.2099.

    >>> days = {...}
    >>> day = 1 # it means first day of ramadan
    >>> days[1]
    datetime(...) # it should return date for this day
    """
    days: dict = {1: START_OF_RAMADAN, }

    for day in range(2, MONTH+1):
        days[day] = days[day-1] + timedelta(1)

    return days


def setUp(app: FastAPI, routers: list):
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    for router in routers:
        app.include_router(router)

    register_tortoise(app, **settings.DATABASE_SETTINGS)
