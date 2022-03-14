import pytest
import typing as t
from json import loads

from utils import *

client = CustomAsyncTestClient()


@pytest.fixture
async def random_region_id():
    response = await client.send_request(GET, "api/regions")
    pytest.RANDOM_REGION_ID = random_index(loads(response.text))


@pytest.fixture
async def regions_count():
    response = await client.send_request(GET, "api/regions")
    pytest.REGIONS_COUNT = len(loads(response.text))


@pytest.mark.anyio
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
            key in ["day", "fajr", "iftar"]
            for data in dates_of_region
            for key in data.keys()
        ]
    ) is True


@pytest.mark.anyio
async def test_region_dates(random_region_id):
    response = await client.send_request(GET, f"api/regions/{pytest.RANDOM_REGION_ID}/dates")
    body: t.List[dict] = loads(response.text)

    assert response.status_code == 200
    assert all(
        [
            key in ["day", "fajr", "iftar"]
            for data in body
            for key in data.keys()
        ]
    ) is True


@pytest.mark.anyio
async def test_today_dates(regions_count):
    response = await client.send_request(GET, "api/dates/today")
    body: t.List[dict] = loads(response.text)

    assert response.status_code == 200
    assert len(body) == pytest.REGIONS_COUNT

    random_region_date: dict = body[random_index(body)-1]
    date = [data[0] for data in random_region_date.values()][0]

    assert all([key in ["day", "iftar", "fajr"] for key in date.keys()])
    assert date["day"] == str(get_current_time())


@pytest.mark.anyio
async def test_today_dates_for_spec_region(random_region_id):
    response = await client.send_request(
        GET,
        f"api/regions/{pytest.RANDOM_REGION_ID}/dates/today"
    )

    body: t.List[dict] = loads(response.text)

    assert response.status_code == 200

    assert all([key in ["day", "iftar", "fajr"] for key in body.keys()])
    assert body["day"] == str(get_current_time())


@pytest.mark.anyio
async def test_spec_day_dates_for_spec_region(random_region_id):
    random_day = random_index(range(1, 30))
    response = await client.send_request(
        GET,
        f"api/regions/{pytest.RANDOM_REGION_ID}/day/{random_day}"
    )

    body: t.List[dict] = loads(response.text)

    assert response.status_code == 200
    assert all([key in ["day", "iftar", "fajr"] for key in body.keys()])
