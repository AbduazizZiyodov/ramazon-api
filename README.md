# **๐ Ramazon-API**

![FASTAPI_LOGO](/screenshots/fastapi.png)

<p align="center"> 
  Assalamu alaikum ๐ <br>
  Ramadan Mubarak. Wishing you a blessed and Happy Ramadan ๐
</p>

## **๐งฐ Setup**

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
$ pip install -r requirements.txt
```

> Or, you can use `poetry` (if you have).

```
$ poetry install
```

# **๐Running Server**

To run fastapi application you will have to use `uvicorn` or `gunicorn`.

### **Uvicorn** ๐ฆ

> `--reload` - reloading for development server.

```bash
$ uvicorn main:api --reload
```

### **Gunicorn** (๐ข)๐ฆ

```bash
$ gunicorn main:api --worker-class uvicorn.workers.UvicornWorker --reload
```

![SWAGGER_UI](/screenshots/swagger-ui.PNG)

- `http://{{ host }}/swagger` - _Swagger UI_

<hr><br>

## **โจMocking Database**

After running server, you should send `GET` request to `/simulate` endpoint from anywhere(swagger UI, curl, postman ...). The results of mocking will be logged on your terminal.

![MOCK_RESULT](/screenshots/mock-result.PNG)

## **๐งช Running Tests**

Running with `poetry`:

```bash
$ poetry run pytest
```

or

```bash
$ pytest
```

![TEST](/screenshots/test-result.PNG)

<p align="center"> 
  ๐ Abduaziz Ziyodov 
</p>
