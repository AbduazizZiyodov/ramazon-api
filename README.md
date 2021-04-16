# Ramazon-API

> **Frontend** (`Angular`): https://ramadan.uz/, source code: https://github.com/AbduazizZiyodov/ramadan.uz-frontend 

> **Backend** (`FastAPI`): https://ramadan.uz/api/v2/docs
## Introduction

_Assalamu alaikum_ 👋 _Ramadan Mubarak. Wishing you a blessed and Happy Ramadan_ :grin:_! Data about times in this month is extremely important. That's why I transferred this information to the API interface. In my opinion, this API will benefit everyone. And below I present my guide._

![FASTAPI_LOGO](/screenshots/fastapi.png)

This API created in **FastAPI + Tortoise ORM**. Nevertheless, its first (`v1`) release created in **Flask + SQLAlchemy**. The reason I switched to **FastAPI**, I couldn't get enough efficiency from `v1`.

## **Setup** :uk:

> **Required:** python +3.6

Clone this repo using `git`

```bash
$ git clone https://github.com/AbduazizZiyodov/ramazon-api.git
# github-cli:
$ gh repo clone AbduazizZiyodov/ramazon-api
```

Go to the project directory. Create virtual enviroment and activate it:

```bash
$ cd ramazon-api/
$ python3 -m venv env && source env/bin/activate
```

Install all required packages using `pip` from `requirements.txt` file.

```bash
$ pip3 install -r requirements.txt
```

The project was created in **FastAPI**, which is considered a new `python3` web framework. In documentatin of framework says that it is expedient to use `uvicorn` as a server. Run server:

```bash
$ uvicorn main:api --reload
```

> `--reload` - if a change is made in the code, the server will load again ( shows efficiency on `debugging` :smile:)

- http://127.0.0.1:8000/api/v2/docs - **API** docs `(1)`

**Screenshots**

![SERVER](/screenshots/running_server.png)
>
> <p align="center"><small>Server is running</small></p>

![SERVER](/screenshots/docs.png)
>
> <p align="center"><small>API docs</small></p>

# API Reference 📗

API (**api/v2**) has 8 endpoints:

- `/` - basic route , the task is to avoid an `404` error 😅
- `/regions` - about regions
- `regions/{id}` - about spec. region
- `/dates` - about dates
- `/regions/{id}/dates` - about spec dates
- `dates/today` - about today
- `regions/{id}/dates/today` - about today for spec region
- `regions/{id}/day/{day}` - about spec data

<hr>

Simple Script for testing:

```python
import requests

def make_request(host, endpoint):
    url = f"http://{host}/api/v2/{endpoint}"
    response = requests.request("GET", url)

    print(response.text)

if __name__ == "__main__":
    host, endpoint = input('host>'), input('endpoint>')
    make_request(host=host, endpoint=endpoint)
```

![SCRIPT](/screenshots/script.png)

<hr>

### 🟢`/regions` [**GET**]

> Annotation: returns all regions with data (only `id`)

```bash
$ curl -X 'GET' \
  '{host}/api/v2/regions' \
  -H 'accept: application/json'
```

Response

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

> Annotation: returns spec region with `id`

```bash
$ curl -X 'GET' \
  '{host}/api/v2/regions/{id}' \
  -H 'accept: application/json'
```

- `id` - **int**

Response:

```json
{
  "hudud_id": 1,
  "hudud": "string"
}
```

### 🟢`/dates` [**GET**]

> Annotation: returns all of the data in database. In this endpoint you can meet responses with `mb` size :grin:

```bash
$ curl -X 'GET' \
  '{host}/api/v2/dates' \
  -H 'accept: application/json'
```

- `id` - **int**

Response:

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

> Annotation: returns about all days data for spec region.

```bash
$ curl -X 'GET' \
  '{host}/api/v2/regions/{region_id}/dates' \
  -H 'accept: application/json'
```

- **region_id** - int

Response:

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

> Annotation: returns all dates about today (for all regions)

```bash
$ curl -X 'GET' \
  '{host}/api/v2/dates/today' \
  -H 'accept: application/json'
```

Rresponse:

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

> Annotation: returns all dates about today for spec region

```bash
$ curl -X 'GET' \
  '{host}/api/v2/dates/today{region_id}' \
  -H 'accept: application/json'
```

- **region_id** - int

Response:

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

> Annotation: returns spec data (by region and day)

```bash
$ curl -X 'GET' \
  '{host}/api/v2/regions/{region_id}/day/{day}' \
  -H 'accept: application/json'
```

- **region_id** - int
- **day** - int

> day - day of ramadan. This means that if `day=1`, then this is the first day of Ramadan, that is `13-th April`.

Response:

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

<hr>

Be healthy 👋

**Author: Abduaziz Ziyodov**

# Kirish 🇺🇿:

_Assalomu alaykum_ 👋 _Ramazon oyi muborak bo'lsin, barcha eng yaxshi tilaklarimni sizga tilab qolaman_ :grin: _Vaqtlarga oid bo'lgan ma'lumotlar ushbu oyda o'ta muhim ahamiyatga ega. Shuning uchun ushbu ma'lumotlarni API interfeysiga ko'chirdim. Mening fikrimcha ushbu APIni barchaga foydasi tegadi. Quyida esa qo'llanmamni keltiraman._

![FASTAPI_LOGO](/screenshots/fastapi.png)

Ushbu API FastAPI + Tortoise ORMda yaratilgan. Lekin, `v1` flask + sqlalchemyda tayyorlangan edi. FastAPIga o'tishimga sabab, `v1`dan yetarlicha samaradorlik olaolmaganimdadir.

## **O'rnatish** 🇺🇿

> **Shart:** python +3.6

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

Loyiha yangi `python3` freymvorki hisoblanuvchi **FastAPI**da yaratilgan. Freymvork qo'llanmasida server sifatida `uvicorn`dan foydalanish maqsadga muvofiqligi haqida aytilgan. `uvicorn` orqali serverni ishga tushuring:

```bash
$ uvicorn main:api --reload
```

> `--reload` - kodda o'zgartirish kiritilsa, server qayta yuklanadi ( `debugging` da rosa qo'l keladi :smile: ).

Endi esa http://127.0.0.1:8000 bo'yicha o'ting.

- http://127.0.0.1:8000/docs - **API** Qo'llanmasi `(1)`

**Skrinshot**

![SERVER](/screenshots/running_server.png)
>
> <p align="center"><small>Server ishlamoqda</small></p>

![SERVER](/screenshots/docs.png)
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

<hr>

Tekshirib ko'rishingiz uchun sodda skript:

```python
import requests

def make_request(host, endpoint):
    url = f"http://{host}/api/v2/{endpoint}"
    response = requests.request("GET", url)

    print(response.text)

if __name__ == "__main__":
    host, endpoint = input('host>'), input('endpoint>')
    make_request(host=host, endpoint=endpoint)
```

![SCRIPT](/screenshots/script.png)

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

<hr>

Salomat bo'ling 👋

**Muallif: Abduaziz Ziyodov**
