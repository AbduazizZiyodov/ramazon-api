from rich import print
from fastapi import APIRouter

from api.utils import generate_days
from api.database.models import Date
from api.database.models import Region
from api.settings import regions_names

mock_router = APIRouter(tags=["Mock"], prefix="/api")


@mock_router.get("/mock")
async def mock_database():
    days = generate_days()

    regions = [
        await Region.create(name=region)
        for region in regions_names
    ]

    for region in regions:
        await region.dates.add(
            *[
                await Date.create(day=day)
                for day in days.values()
            ]
        )
        dates = await region.dates
        print(
            f"[bold green]:fire: Region: [bold red]{region.name} {len(dates)}")

    print(
        f"[bold cyan] Success! Total regions: {len(regions)} :tada: ")

    return {"success": True}
