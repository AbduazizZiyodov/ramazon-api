from typing import List
import pytz
from datetime import (
    date,
    datetime,
    timedelta
)

TITLE: str = "RamadanAPI"

DESCRIPTION: str = """
**API** for Ramadan Calendar(2021). 
<br> Assalamu alaikum👋 Ramadan Mubarak. 
Wishing you a blessed and Happy Ramadan! 
<br> Data about times in this month is extremely important. 
<br> That's why I transferred this information to the **API** interface. 
This **API** will benefit everyone!
<br> **Author: Abduaziz Ziyodov**
"""


DATABASE_SETTINGS = {
    "db_url": "sqlite://api/database/database.sqlite",
    "modules": {
        'models': ['api.database.models']
    },
    "generate_schemas": True,
    "add_exception_handlers": True,
}

FASTAPI_SETTINGS = {
    "title": TITLE,
    "openapi_tags": [
        {
            "name": "Regions",
            "description": "Operations with regions"
        },
        {
            "name": "Dates",
            "description": "Operations with dates"
        }
    ],
    "version": "3.0.0",
    "description": DESCRIPTION,
    "redoc_url": None,
    "docs_url": '/swagger',
    "debug": False
}

TIMEZONE = "Asia/Tashkent"

regions_names: List[str] = [
    # Toshkent
    'Toshkent', 'Angren', 'Piskent', 'Bekobod', 'Parkent', "G'azalkent", 'Olmaliq',
    "Boka", "Yangiyo'l", 'Nurafshon',
    # Buxoro
    'Buxoro', 'Gazli', "G'ijduvon", "Qorako'l", 'Jondor',
    # Fargona
    "Farg'ona", "Marg'ilon", "Qo'qon", "Quva", 'Rishton', "Bog'dod", "Oltiariq",
    # Sirdaryo
    'Guliston', 'Sardoba', 'Sirdaryo', 'Boyovut', 'Paxtaobod',
    # Jizzax
    'Jizzax', 'Zomin', 'Forish', "G'allaorol", "Do'stlik",
    # Navoiy
    "Navoiy", 'Zarafshon', 'Konimex', 'Nurota', 'Uchquduq',
    # Namangan
    'Namangan', 'Chortoq', 'Chust', 'Pop', "Uchqo'rg'on",
    # Qoraqalpogiston
    'Nukus', "Mo'ynoq", "Taxtako'pir", "To'rtkol", "Qo'ng'irot",
    # Samarqand
    'Samarqand', 'Ishtixon', 'Mirbozor', "Kattaqo'rg'on", 'Urgut',
    # Surxondaryo
    'Termiz', 'Boysun', 'Denov', 'Sherobod', "Sho'rchi",
    # Qashqadaryo
    'Qarshi', 'Dehqonobod', 'Muborak', 'Shahrisabz', "G'uzor",
    # Andijon
    'Andijon', 'Xonobod', 'Shahrixon', "Xo'jaobod", 'Asaka', 'Marhamat', "Paytug'",
    # Xorazm
    'Urganch', 'Hazorasp', 'Xonqa', 'Yangibozor', 'Shovot', 'Xiva'
]


def get_current_time() -> date:
    """
    Returns current DateTime according to timezone
    """
    return datetime.now(pytz.timezone(TIMEZONE)).date()


MONTH: int = 30  # days

if FASTAPI_SETTINGS.get("debug"):
    START_OF_RAMADAN: date = get_current_time()
    END_OF_RAMADAN: date = START_OF_RAMADAN + timedelta(days=MONTH)
else:
    START_OF_RAMADAN: date = date(2022, 4, 2)
    END_OF_RAMADAN: date = START_OF_RAMADAN + timedelta(MONTH)
