import pytest
import pytest_asyncio

import typing as t
from json import loads

from utils import *

client = CustomAsyncTestClient()

REQUIRED_FIELDS = ["day", "fajr", "iftar", "day_of_ramadan", "day_full"]


@pytest_asyncio.fixture
async def random_region_id():
    response = await client.send_request(GET, "api/regions")
    pytest.RANDOM_REGION_ID = random_index(loads(response.text))


@pytest_asyncio.fixture
async def regions_count():
    response = await client.send_request(GET, "api/regions")
    pytest.REGIONS_COUNT = len(loads(response.text))


@pytest.mark.asyncio
async def test_dates():
    response = await client.send_request(GET, "api/dates")
    body: t.List[dict] = loads(response.text)
    dates_of_region: dict = body[random_index(body)-1]
    dates_of_region: t.List[dict] = [
        key
        for key in dates_of_region.values()
    ][0]

    assert response.status_code == 200
    assert all(
        [
            key in REQUIRED_FIELDS
            for data in dates_of_region
            for key in data.keys()
        ]
    ) is True


@pytest.mark.asyncio
async def test_region_dates(random_region_id):
    response = await client.send_request(GET, f"api/regions/{pytest.RANDOM_REGION_ID}/dates")
    body: t.List[dict] = loads(response.text)

    assert response.status_code == 200
    assert all(
        [
            key in REQUIRED_FIELDS
            for data in body
            for key in data.keys()
        ]
    ) is True


@pytest.mark.asyncio
async def test_today_dates(regions_count):
    response = await client.send_request(GET, "api/dates/today")
    body: t.List[dict] = loads(response.text)

    assert response.status_code == 200
    assert len(body) == pytest.REGIONS_COUNT

    random_region_date: dict = body[random_index(body)-1]
    date = [data[0] for data in random_region_date.values()][0]

    assert all(
        [
            key in REQUIRED_FIELDS
            for key in date.keys()
        ]
    )
    assert date["day"] == str(get_current_time())


@pytest.mark.asyncio
async def test_today_dates_for_spec_region(random_region_id):
    response = await client.send_request(
        GET,
        f"api/regions/{pytest.RANDOM_REGION_ID}/dates/today"
    )

    body: t.List[dict] = loads(response.text)

    assert response.status_code == 200

    assert all(
        [
            key in REQUIRED_FIELDS
            for key in body.keys()
        ]
    )
    assert body["day"] == str(get_current_time())

DAYS_IN_MONTH: int = 30


@pytest.mark.asyncio
async def test_spec_day_dates_for_spec_regions(regions_count):
    for region_id in range(1, pytest.REGIONS_COUNT+1):
        for day in range(1, DAYS_IN_MONTH+1):
            response = await client.send_request(
                GET,
                f"api/regions/{region_id}/day/{day}"
            )

            body: t.List[dict] = loads(response.text)

            assert response.status_code == 200
            assert all(
                [
                    key in REQUIRED_FIELDS
                    for key in body.keys()
                ]
            )
