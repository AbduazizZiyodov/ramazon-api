import pytest
import pytest_asyncio

import typing as t
from json import loads

from utils import *

client = CustomAsyncTestClient()


@pytest_asyncio.fixture
async def random_region_id():
    response = await client.send_request(GET, "api/regions")
    pytest.RANDOM_REGION_ID = random_index(loads(response.text))


@pytest.mark.asyncio
async def test_list_regions():
    response = await client.send_request(GET, "api/regions")
    body: t.Optional[t.List[dict]] = loads(response.text)

    assert response.status_code == 200
    assert "id" in body[random_index(body)].keys()


@pytest.mark.asyncio
async def test_region_detailed(random_region_id):
    response = await client.send_request(
        GET,
        f"api/regions/{pytest.RANDOM_REGION_ID}"
    )

    body: t.Optional[dict] = loads(response.text)

    assert response.status_code == 200

    required_keys = ["id", "name"]

    assert all([key in required_keys for key in body.keys()]) is True
