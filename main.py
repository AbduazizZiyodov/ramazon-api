from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.pydantic import pydantic_model_creator
# -------------------------------------------------------- #
from database.models import Region
from database.models import Date
from helpers import configure_db
from helpers import http_404, current


api = FastAPI(title="RamazonAPI")

api.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

configure_db(app=api)

Region_pydantic = pydantic_model_creator(Region, name="Region")
Date_pydantic = pydantic_model_creator(Date, name="Date")


@api.get('/')
async def home_page():
    return JSONResponse({
        "muvaffaqiyat": True,
        "Sarlavha": "Ramazon-API",
        "Muallif": "Abduaziz Ziyodov",
        "GitHub": "https://github.com/AbduazizZiyodov/ramazon-api"
    })


@api.get('/api/v2/regions')
async def get_regions():
    return await Region.all()


@api.get('/api/v2/regions/{id}')
async def get_region_by_id(id: int):
    data = Region.filter(hudud_id=id)
    resp: Region = await data.get_or_none() or http_404()
    return resp.full_format()


@api.get('/api/v2/dates')
async def get_dates():
    regions = await Region.all()
    response = []
    for region in regions:
        query = await Date.filter(hudud=region.hudud)
        response.append({
            "hudud": region.hudud,
            "hudud_id": region.hudud_id,
            "ma'lumotlar": [q.full_format() for q in query]
        })
    return response


async def get_current(region: str):
    data = await Date.filter(kun_full=current, hudud=region).first()
    if data is None:
        return http_404()

    return data.response_format()


@api.get('/api/v2/dates/today')
async def get_dates_today():
    query = await Region.all()
    return [await get_current(region=region.hudud) for region in query]


@api.get('/api/v2/regions/{id}/dates/today')
async def get_dates_today_by_region(id: int):
    data = await Region.filter(hudud_id=id).first()
    if data is None:
        http_404()
    today_data = await Date.filter(kun_full=current, hudud=data.hudud).first()
    if today_data is None:
        return http_404()

    return today_data.full_format()


@api.get('/api/v2/regions/{id}/dates')
async def get_dates_by_region(id: int):
    region = await Region.filter(hudud_id=id).first()
    if region is None:
        return http_404()
    dates = await Date.filter(hudud=region.hudud)

    return [d.full_format() for d in dates]


@api.get('/api/v2/regions/{region_id}/day/{day}')
async def get_spec_data(region_id: int, day: int):
    region = await Region.filter(hudud_id=region_id).first()
    if region is None:
        return http_404()
    date = await Date.filter(hudud=region.hudud, kun=day).first()

    if date is None:
        return http_404()

    return date.full_format()