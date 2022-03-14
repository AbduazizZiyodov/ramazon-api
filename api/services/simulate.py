import subprocess
from rich import print

from fastapi import APIRouter
from api.utils import generate_days

from api.database.models import Date
from api.database.models import Region

router = APIRouter(tags=["Mocking (simulation)"])


@router.get("/simulate")
async def simulate():
    subprocess.call(["rm", "api/database/database.sqlite"])
    days = generate_days()

    regions: list[str] = [
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
        'Mingbuloq', 'Namangan', 'Chortoq', 'Chust', 'Pop', "Uchqo'rg'on",
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

    region_objects = [
        await Region.create(name=region)
        for region in regions
    ]

    for region in region_objects:
        await region.dates.add(
            *[
                await Date.create(day=day)
                for day in days.values()
            ]
        )
        dates = await region.dates
        print(
            f"[bold green]:fire: Region: [bold red]{region.name} {len(dates)}")

    print(
        f"[bold cyan] Success! Total regions: {len(region_objects)} :tada: ")

    return {}
