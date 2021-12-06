from typing import Dict
from typing import List

from pydantic import BaseModel

from datetime import date
from datetime import datetime


class Region(BaseModel):
    id: int
    name: str


class Date(BaseModel):
    day: date

    fajr: datetime
    iftar: datetime


class Dates(BaseModel):
    __root__: Dict[str, List[Date]]