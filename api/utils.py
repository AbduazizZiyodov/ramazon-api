from datetime import timedelta

from api.settings import MONTH
from api.settings import START_OF_RAMADAN



def generate_days() -> dict:
    """
    Generates days for Ramadan.
    e.g First day of ramadan may be 01.12.2099.

    >>> days = {...}
    >>> day = 1 # it means first day of ramadan
    >>> days[1]
    datetime(...) # it should return date for this day
    """
    days: dict = {1: START_OF_RAMADAN, }

    for day in range(2, MONTH+1):
        days[day] = days[day-1] + timedelta(1)

    return days
