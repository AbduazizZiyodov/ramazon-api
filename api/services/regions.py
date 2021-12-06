from typing import List
from fastapi import APIRouter

import api.schemas as schemas
from api.database.models import Region


router = APIRouter(
    tags=["Regions"],
    prefix='/api'
)


@router.get('/regions', response_model=List[schemas.Region])
async def regions():
    return await Region.all()


@router.get('/regions/{region_id}', response_model=schemas.Region)
async def region_detailed(region_id: int):
    return await Region.get(pk=region_id)
