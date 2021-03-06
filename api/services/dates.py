from typing import List
from datetime import date

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

import api.schemas as schemas
from api.database.models import *

from api.utils import generate_days
from api.utils import get_current_time

router = APIRouter(
    tags=["Dates"],
    prefix="/api"
)

days = generate_days()


@router.get("/today",response_model=schemas.Today)
async def get_today():
    return get_current_time(full_format=True)


@router.get(
    "/dates",
    response_model=List[schemas.Dates]
)
async def get_all_dates():
    return [
        {region.name: await region.dates}
        for region in await Region.all()
    ]


@router.get(
    "/regions/{region_id}/dates",
    response_model=List[schemas.Date]
)
async def get_dates_by_region(region_id: int):
    region: Region = await Region.get(pk=region_id)

    return await region.dates


@router.get(
    "/dates/today",
    response_model=List[schemas.TodayDates]
)
async def get_dates_today():
    current_day: date = get_current_time()

    return [
        {
            region.name: await region.dates.filter(day=current_day).first()
        }
        for region in await Region.all()
    ]


@router.get(
    "/regions/{region_id}/dates/today",
    response_model=schemas.Date
)
async def get_today_dates_by_region(region_id: int):
    current_day: date = get_current_time()
    region: Region = await Region.get(pk=region_id)

    return await region.dates.filter(day=current_day).first()


@router.get(
    "/regions/{region_id}/day/{day}",
    response_model=schemas.Date
)
async def get_specific_date(region_id: int, day: int):
    day_of_ramadan: int = days.get(day)

    region: Region = await Region.get(pk=region_id)
    _date: Date = await region.dates.filter(day=day_of_ramadan).first()

    if _date is None:
        raise HTTPException(404)

    return _date
