# Portfolio Backend

This project consist of a **Django Rest Framework (DRF) API** to manage a portfolio(projects and blog), to be consumed by a front end

## Requirements

- **Python 3.9+**
- **PostgreSQL(optional) or SQLite**


## Backend Installation

```sh
python -m venv env
source env/bin/activate #On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### Create a .env or Set Your enviroments on settings.py
example:

```sh
SECRET_KEY="your-secret-key"
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  
ALLOWED_HOSTS=*
```



### Apply migrations
```sh
python manage.py makemigrations
python manage.py migrate

```
### Run Server

```sh
python manage.py runserver

```


