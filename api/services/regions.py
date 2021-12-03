import schemas
from typing import List
from fastapi import APIRouter

from database.models import Region
from helpers import http_404


router = APIRouter(
    tags=["Regions"],
    prefix='/api/v2'
)


@router.get('/regions',
        response_model=List[schemas.Region])
async def get_regions():
    return await Region.all()


@router.get('/regions/{id}',
        response_model=schemas.Region)
async def get_region_by_id(id: int):
    data = Region.filter(hudud_id=id)
    resp: Region = await data.get_or_none() or http_404()

    return resp.full_format()
