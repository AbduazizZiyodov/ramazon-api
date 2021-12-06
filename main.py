from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tortoise.contrib.fastapi import register_tortoise

from api import settings
from api.services.dates import router as dates_router
from api.services.regions import router as regions_router
from api.services.simulate import router as simulate_router

api = FastAPI(**settings.FASTAPI_SETTINGS)

api.include_router(dates_router)
api.include_router(regions_router)

if settings.TESTING:
    api.include_router(simulate_router)

api.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(api, **settings.DATABASE_SETTINGS)
