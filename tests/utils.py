import pytz
import httpx
import typing as t
from random import randint

from datetime import (
    date,
    datetime
)


GET, POST, PUT, PATCH, DELETE = \
    "GET", "POST", "PUT", "PATCH", "DELETE"

PRODUCTION: bool = False


class CustomAsyncTestClient:
    API_URL: str = "http://127.0.0.1:8000" if not PRODUCTION else ""

    async def send_request(
        self,
        method: str,
        endpoint: str,
        data: t.Optional[dict] = {},
        headers: t.Optional[httpx.Headers] = httpx.Headers({})
    ) -> httpx.Response:

        url: str = f"{self.API_URL}/{endpoint}"

        async with httpx.AsyncClient() as client:
            response: httpx.Response = await client\
                .request(method, url, data=data, headers=headers)

        return response


def random_index(obj): return randint(1, len(obj))  # obj should be iterable


def get_current_time() -> date:
    """
    Returns current DateTime according to timezone
    """
    if PRODUCTION:
        return datetime.now(pytz.timezone("Asia/Tashkent")).date()
    return date(2022, 4, 24)


__all__ = ["CustomAsyncTestClient", "random_index",
           "get_current_time", "GET", "POST", "PUT", "PATCH", "DELETE"]
