# **🕌 Ramazon-API**

![FASTAPI_LOGO](/screenshots/fastapi.png)

<p align="center"> 
  _Assalamu alaikum_ 👋 _Ramadan Mubarak. Wishing you a blessed and Happy Ramadan_ 😀
</p>

## **🧰 Setup**

> **Required:** python +3.6

Clone this repository:

```bash
# git
$ git clone https://github.com/AbduazizZiyodov/ramazon-api.git
```

```bash
# github-cli:
$ gh repo clone AbduazizZiyodov/ramazon-api
```

Go to the project directory. Create virtual enviroment and activate it:

```bash
$ cd ramazon-api/
$ python -m venv env && source env/bin/activate

# env/Scripts/activate - windows
```

Install all required packages using `pip` from `requirements.txt` file.

```bash
$ pip3 install -r requirements.txt
```

# **🚀Running Server**

To run fastapi application you will have to use `uvicorn` or `gunicorn`.

**Uvicorn** 🦄:

```bash
$ uvicorn main:api
```

**Gunicorn** (🟢)🦄:

```bash
$ gunicorn main:api --worker-class uvicorn.workers.UvicornWorker
```

![SWAGGER_UI](/screenshots/swagger-ui.png)

- `http://{{ host }}/swagger` - _Swagger UI_

<hr><br>

<p align="center"> 
  🐍 Abduaziz Ziyodov 
</p>
