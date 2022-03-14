import pytest
from utils import *


client = CustomAsyncTestClient()


@pytest.mark.anyio
async def test_base_route():
    response = await client.send_request(GET, "")

    assert response.status_code == 200
    assert response.text is not None


@pytest.mark.anyio
async def test_swagger_ui():
    response = await client.send_request(GET, "swagger")

    assert response.status_code == 200
    assert response.text is not None
