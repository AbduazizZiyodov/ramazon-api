from fastapi import FastAPI

from api import settings
from api.utils import setUp
from api.services.dates import router as dates_router
from api.services.regions import router as regions_router
from api.services.mock import mock_router

api = FastAPI(**settings.FASTAPI_SETTINGS)

routers = [dates_router, regions_router]

if api.debug:
    routers.append(mock_router)

setUp(api, routers)


@api.get("/", tags=["Base Route"])
async def base_route():
    return {"message": "Ramadan API is working 🔥"}
