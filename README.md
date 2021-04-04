# 1. Ramazon-API

### **O'rnatish** 🇺🇿

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
* http://127.0.0.1:8000/docs - **API** Qo'llanmasi `(1)`
* http://127.0.0.1:8000/redoc - **API** Qo'llanmasi `(2)`


**Skrinshot**


