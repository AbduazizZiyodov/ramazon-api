# Ramazon-API

## Kirish:

*Assalomu alaykum* 👋 *Ismim Abduaziz, ramazon muborak* :grin: *Ushbu oyda barcha ro'za tutishadi, ularga esa saharlik va iftorlik vaqtlarini bilish o'ta muhim. Dasturchi sifatida xissa qo'sha olishim uchun, ushbu ma'lumotlarni API interfeysiga ko'chirdim. APIdan o'z loyihalaringizda bemalol foydalanishingiz mumkin, quyida o'rnatish va foydalanishga bag'ishlangan qisqagini qo'llanmamni keltiraman, marhamat:*

![FASTAPI_LOGO](/screenshots/fastapi.png)

Ushbu API FastAPI + Tortoise ORMda yaratilgan. Lekin, `v1` flask + sqlalchemyda tayyorlangan edi. FastAPIga o'tishimga sabab, `v1`dan yetarlicha samaradorlik olaolmaganimdadir.

## **O'rnatish** 🇺🇿

Ushbu repozitoriyani `git` buyruqlari asosida ko'chirib oling:

```bash
$ git clone https://github.com/AbduazizZiyodov/ramazon-api.git
# github-cli:
$ gh repo clone AbduazizZiyodov/ramazon-api
```

Loyiha katalogiga o'tib, virtual muhitni yarating va uni faollashtiring:

```bash
$ cd ramazon-api/
$ python3 -m venv env && source env/bin/activate
```

Barcha kerakli modullar ro'yxati loyiha katalogidagi `requirements.txt` faylida keltirilgan. `pip` yordamida ularni o'rnating:

```bash
$ pip3 install -r requirements.txt
```

Loyiha yangi `python3` freymvorki hisoblanuvchi **FastAPI**da yaratilgan. Freymvork qo'llanmasida server sifatida `uvicorn`dan foydalanish maqsadga muvofiqligi haqida aytilgan (hypercorn, gunicorn kabi serverlar ham mavjud). `uvicorn` orqali serverni ishga tushuring:

```bash
$ uvicorn main:api --reload
```

> `--reload` - kodda o'zgartirish kiritilsa, server qayta yuklanadi ( `debugging` da rosa qo'l keladi :smile: ).

Endi esa http://127.0.0.1:8000 bo'yicha o'ting.

- http://127.0.0.1:8000/docs - **API** Qo'llanmasi `(1)`

**Skrinshot**

> ![SERVER](/screenshots/running_server.png)
>
> <p align="center"><small>Server ishga tushdi</small></p>

> ![SERVER](/screenshots/docs.png)
>
> <p align="center"><small>API qo'llanmasi</small></p>

# API 📗

API (**api/v2**) 8ta endpointga ega:

- `/` - basic route deb nomladim, vazifasi shunchaki `/` bo'yicha o'tilganda `404` bermaslik 😅
- `/regions` - hududlar haqida
- `regions/{id}` - maxsus hudud haqida
- `/dates` -vaqtlar haqida
- `/regions/{id}/dates` - maxsus hududning vaqtlari haqida
- `dates/today` - bugungi vaqtlar haqida
- `regions/{id}/dates/today` - maxsus hududning bugungi vaqtlari haqida
- `regions/{id}/day/{day}` - maxsus hududning maxsus kuni haqida

## **Region** endpointlari :

<hr>

### 🟢`/regions` [**GET**]

> Izoh: Barcha hududlar ro'yxatini qaytaradi (+`id`lari bilan birgalikda)

```bash
$ curl -X 'GET' \
  '{host}/api/v2/regions' \
  -H 'accept: application/json'
```

Javob (response):

```json
[
  {
    "hudud_id": 1,
    "hudud": "string"
  },
  {
    "hudud_id": 0,
    "hudud": "string"
  }
  ...
]
```

### 🟢`/regions/{id}` [**GET**]

> Izoh: Maxsus hudud haqidagi ma'lumotni qaytaradi (+`id` bilan birgalikda)

```bash
$ curl -X 'GET' \
  '{host}/api/v2/regions/{id}' \
  -H 'accept: application/json'
```

- `id` - **int**

Javob (response):

```json
{
  "hudud_id": 1,
  "hudud": "string"
}
```

### 🟢`/dates` [**GET**]

> Izoh: ma'lumotlar omboridagi ma'lumotlarni barchasini qaytaradi. Aynan shu punktda `mb` hajmga ega responselarni uchratishingiz mumkin :grin:

```bash
$ curl -X 'GET' \
  '{host}/api/v2/dates' \
  -H 'accept: application/json'
```

- `id` - **int**

Javob (response):

```json
[
  {
    "hudud": "string1",
    "hudud_id": 1,
    "data": [
      {
        "kun": "string",
        "hafta_kuni": "string",
        "izoh": "string",
        "vaqtlar": {
          "iftorlik": "string",
          "saharlik": "string"
        }
      },
            {
        "kun": "string",
        "hafta_kuni": "string",
        "izoh": "string",
        "vaqtlar": {
          "iftorlik": "string",
          "saharlik": "string"
        }
      }
      ...
    ]
  },
  {
    "hudud": "string2",
    "hudud_id": 2,
    "data": [
      {
        "kun": "string",
        "hafta_kuni": "string",
        "izoh": "string",
        "vaqtlar": {
          "iftorlik": "string",
          "saharlik": "string"
        }
      },
            {
        "kun": "string",
        "hafta_kuni": "string",
        "izoh": "string",
        "vaqtlar": {
          "iftorlik": "string",
          "saharlik": "string"
        }
      }
      ...
    ]
  }
  ...
]
```

### 🟢`/regions/{region_id}/dates` [**GET**]

> Izoh: Ma'lum bir hududga oid bo'lgan barcha kunlar haqidagi ma'lumotlarni qaytaradi

```bash
$ curl -X 'GET' \
  '{host}/api/v2/regions/{region_id}/dates' \
  -H 'accept: application/json'
```

- **region_id** - int

Javob (response):

```json
[
  {
    "kun": "string1",
    "hafta_kuni": "string1",
    "izoh": "string",
    "vaqtlar": {
      "iftorlik": "string",
      "saharlik": "string"
    }
  },
  {
    "kun": "string2",
    "hafta_kuni": "string2",
    "izoh": "string",
    "vaqtlar": {
      "iftorlik": "string",
      "saharlik": "string"
    }
  }
]
```

### 🟢`/dates/today` [**GET**]

> Izoh: Bugungi kunga oid bo'lgan barcha ma'lumotlarni qaytaradi (barcha hududlar uchun)

```bash
$ curl -X 'GET' \
  '{host}/api/v2/dates/today' \
  -H 'accept: application/json'
```

Javob (response):

```json
[
  "RegionName1": {
    "kun": "string",
    "hafta_kuni": "string",
    "izoh": "string",
    "vaqtlar": {
      "iftorlik": "string",
      "saharlik": "string"
    }
  },
    "RegionName2": {
    "kun": "string",
    "hafta_kuni": "string",
    "izoh": "string",
    "vaqtlar": {
      "iftorlik": "string",
      "saharlik": "string"
    }
  }
  ...
]
```

### 🟢`/dates/today/{region_id}` [**GET**]

> Izoh: Bugungi kunga oid bo'lgan maxsus hududga oid ma'lumotni qaytaradi.

```bash
$ curl -X 'GET' \
  '{host}/api/v2/dates/today{region_id}' \
  -H 'accept: application/json'
```

- **region_id** - int

Javob (response):

```json
{
  "kun": "string",
  "hafta_kuni": "string",
  "izoh": "string",
  "vaqtlar": {
    "iftorlik": "string",
    "saharlik": "string"
  }
}
```

### 🟢`/regions/{region_id}/day/{day}` [**GET**]

> Izoh: Ma'lum bir hududga oid bo'lgan maxsus kunga oid ma'lumotni qaytaradi

```bash
$ curl -X 'GET' \
  '{host}/api/v2/regions/{region_id}/day/{day}' \
  -H 'accept: application/json'
```

- **region_id** - int
- **day** - int

> day - ramazon oyining kuni. day=1 bo'lsa , bu ramazon oyining birinchi kuni ya'ni 13-aprel demakdir.

Javob (response):

```json
{
  "kun": "string",
  "hafta_kuni": "string",
  "izoh": "string",
  "vaqtlar": {
    "iftorlik": "string",
    "saharlik": "string"
  }
}
```
