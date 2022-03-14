from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tortoise.contrib.fastapi import register_tortoise

from . import settings
from .services.dates import router as dates_router
from .services.regions import router as regions_router
from .services.simulate import router as simulate_router

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


@api.get("/", tags=["Base Route"])
async def base_route():
    return {"message": "Ramadan API is working 🔥"}

register_tortoise(api, **settings.DATABASE_SETTINGS)
