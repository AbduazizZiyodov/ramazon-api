from datetime import date, time
from pydantic import BaseModel


class Region(BaseModel):
    hudud_id: int
    hudud: str


class Date(BaseModel):
    id: int
    hudud: str
    kun: str
    hafta_kun: str
    kun_full: date
    fajr: time
    iftar: time
