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
    day_full: str
    day_of_ramadan: int

    fajr: datetime
    iftar: datetime


class Dates(BaseModel):
    __root__: Dict[str, List[Date]]


class TodayDates(BaseModel):
    __root__: Dict[str, Date]


class AdditionalInfo(BaseModel):
    day: int
    month: str
    weekday: str
    day_of_ramadan: int


class Today(BaseModel):
    date: date
    additional_info: AdditionalInfo
