from typing import List
from datetime import date, time
from pydantic import BaseModel


class Region(BaseModel):
    hudud_id: int
    hudud: str

class Vaqt(BaseModel):
    iftorlik: time
    saharlik:   time

class Date(BaseModel):
    kun: str
    hafta_kuni: str
    izoh: str
    vaqtlar:  Vaqt

class Dates(BaseModel):
    hudud: str
    hudud_id: int
    data: List[Date]