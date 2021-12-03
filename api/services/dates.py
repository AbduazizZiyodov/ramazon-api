import pytz
import schemas
from typing import List
from fastapi import APIRouter
from datetime import datetime

from database.models import Date
from database.models import Region
from helpers import http_404


router = APIRouter(
    tags=["Dates"],
    prefix='/api/v2'
)

@router.get('/dates',
        response_model=List[schemas.Dates])
async def get_dates():
    regions = await Region.all()
    response = []
    for region in regions:
        query = await Date.filter(hudud=region.hudud)
        response.append({
            "hudud": region.hudud,
            "hudud_id": region.hudud_id,
            "data": [q.full_format() for q in query]})
    return response


async def get_current(region: str):
    current = datetime.now(pytz.timezone('Asia/Tashkent')).strftime("%Y-%m-%d")
    data = await Date.filter(kun_full=current, hudud=region)\
        .first()
    if data is None:
        return http_404()

    return data.response_format()


@router.get('/dates/today')
async def get_dates_today():
    query = await Region.all()
    return [await get_current(region=region.hudud) for region in query]


@router.get('/regions/{id}/dates/today',
        response_model=schemas.Date)
async def get_dates_today_by_region(id: int):
    current = datetime.now(pytz.timezone('Asia/Tashkent')).strftime("%Y-%m-%d")
    data = await Region.filter(hudud_id=id).first()
    if data is None:
        http_404()
    today_data = await Date\
        .filter(kun_full=current, hudud=data.hudud).first()

    if today_data is None:
        return http_404()

    return today_data.full_format()


@router.get('/regions/{id}/dates',
        response_model=List[schemas.Date])
async def get_dates_by_region(id: int):
    region = await Region.filter(hudud_id=id).first()

    if region is None:
        return http_404()

    dates = await Date.filter(hudud=region.hudud)

    return [d.full_format() for d in dates]


@router.get('/regions/{region_id}/day/{day}',
        response_model=schemas.Date)
async def get_spec_data(region_id: int, day: int):
    region = await Region.filter(hudud_id=region_id).first()

    if region is None:
        return http_404()

    date = await Date.filter(hudud=region.hudud, kun=day)\
                                                .first()

    if date is None:
        return http_404()

    return date.full_format()