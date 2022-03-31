import pytz
from rich import print
from fastapi import FastAPI
from datetime import date
from datetime import datetime
from datetime import timedelta
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from api import settings
from api.database.models import *


def generate_days() -> dict:
    """
    Generates days for Ramadan.
    e.g First day of ramadan = 01.12.2099.

    >>> days = {...}
    >>> day = 1 # it means first day of ramadan
    >>> days[1]
    datetime(...) # it should return date for this day
    """
    days: dict = {1: settings.START_OF_RAMADAN, }

    for day in range(2, settings.MONTH+1):
        days[day] = days[day-1] + timedelta(1)

    return days


def get_current_time(full_format: bool = False) -> date:
    """
    Returns current Datetime according to timezone
    """
    def format_month_weekday(date: date):

        day_of_ramadan = [
            key
            for key, value in generate_days().items()
            if value == date
        ][0]
        return {
            "date": date,
            "additional_info": {
                "month": settings.MONTHS.get(date.month),
                "day": date.day,
                "weekday": settings.DAYS.get(date.weekday()),
                "day_of_ramadan": day_of_ramadan,
            }
        }

    if settings.FASTAPI_SETTINGS["debug"]:
        now = date(2022, 4, 24)
        return format_month_weekday(now) if full_format else now

    else:
        now = datetime.now(pytz.timezone(settings.TIMEZONE)).date()

    return format_month_weekday(now) if full_format else now


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


def print_region(region, dates):
    print(
        f"[bold green]:fire: Region: [bold red]{region.name} {len(dates)}")


def print_total(regions):
    print(
        f"[bold cyan] Success! Total regions: {len(regions)} :tada: ")


def to_datetime(_date: date, data: dict) -> datetime:
    def helper(time: str):
        return datetime(
            year=_date.year,
            month=_date.month,
            day=_date.day,
            hour=int(time[:2]),
            minute=int(time[3:])
        )

    return dict(
        fajr=helper(data["saharlik"]),
        iftar=helper(data["iftorlik"])
    )
