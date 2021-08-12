from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# -------------------------------------------------------- #
from helpers import metadata
from helpers import configure_db
from core.dates import dates
from core.regions import regions


api = FastAPI(
    title="RamazonAPI",
    openapi_tags=metadata,
    version="2.0.0",
    description="**API** for Ramadan Calendar(2021). <br> Assalamu alaikum👋 Ramadan Mubarak. Wishing you a blessed and Happy Ramadan! <br> Data about times in this month is extremely important. <br> That's why I transferred this information to the **API** interface. In my opinion, this **API** will benefit everyone. <br> **Author: Abduaziz Ziyodov**",
    openapi_url="/api/v2/openapi.json",
    redoc_url=None,
    docs_url='/api/v2/docs'
)

api.include_router(regions.router)
api.include_router(dates.router)

api.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

configure_db(app=api)
