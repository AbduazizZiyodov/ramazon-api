import sentry_sdk
from os import getenv
from fastapi import FastAPI
from dotenv import load_dotenv

from api import settings
from api.utils import setUp
from api.services.dates import router as dates_router
from api.services.regions import router as regions_router
from api.services.mock import mock_router

api = FastAPI(**settings.FASTAPI_SETTINGS)

routers = [dates_router, regions_router]

if api.debug:
    routers.append(mock_router)

@api.on_event("startup")
async def startup_event():
    load_dotenv(), setUp(api, routers)
    sentry_sdk.init(
        getenv("SENTRY_DSN"),
        traces_sample_rate=1.0
    )


@api.get("/", tags=["Base Route"])
async def base_route():
    return {"message": "Ramadan API is working 🔥"}
