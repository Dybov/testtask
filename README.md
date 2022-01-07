# Install

## Download

If you have Git installed:
```console
git clone https://github.com/Dybov/testtask
cd testtask
```

Or download this project via [direct link](https://github.com/Dybov/testtask/archive/refs/heads/master.zip) and unzip it.

## Set up venv

### Unix/Linux

```console
python3 -m venv --prompt testtask env
source env/bin/activate
```

### Windows

```cmd
py -m venv --prompt testtask env
.\env\Scripts\activate
```

### Other

Or use virtualenv and/or virtualenvwrapper as you are used to.

## Install packages

Use python install package for both nix and win
```console
pip install -r requirements.txt
```

>If you have a trouble while installing psycopg2, try **pip install psycopg2-binary** instead 

# Setup database

[PostgreSQL](https://www.postgresql.org/) is required in the task.
Installation as well as creation and setting of users are out of scope of the task.

## Use default config

For running out of box:
1. Create in your PostgreSQL user **flask** with password **flask**
2. Ensure PostgreSQL is running at localhost:5432 (by default)

## Provide DB config

If you already have user or if you have another server/port provide it in DATABASE_URI Envrimoment variable or in config files

### Envrimoment variable
\*nix:
```console
export DATABASE_URI=postgresql://USERNAME:PASSWORD@SERVER:PORT/DATABASE
```
win:
```cmd
set DATABASE_URI=postgresql://USERNAME:PASSWORD@SERVER:PORT/DATABASE
```

### Config file

Change in your **project_folder/config/dev.py** next line
```python
    DATABASE_URI = 'postgresql://flask:flask@localhost/testtaskdb'
```
to
```python
    DATABASE_URI = 'postgresql://USERNAME:PASSWORD@SERVER:PORT/DATABASE'
```

# Run

Before first run, initialize database with
```console
python init_db.py
```

Database will filled at init step with seed provided at fixture/*

Initial user is superuser with username **groot** and password **iamgroot**. Superuser can add/change/delete any stuff without setting permissions.

To run:
```console
python app.py
```
>Note: If in your \*nix OS **python** command is used for python 2 use **python3** instead
>If using **flask run** instead, then do not forget to add environment variable **FLASK_ENV=development**  

After adding **project_folder/config/prod.py** file with **ProdConfig** class it will run using that config.

# Unittest

Unittesting is out of scope of the task.

# Deploy

Deployment is out of scope of the task.

# Summary

Task #1 is completed:
- There is more than 2 pages
- Features add/change/delete user are provided with permissions
- Unauthorized access to user_list/add/change/delete pages is prohibited. add/change/delete are allowed only users with appropriate permissions
- There is AJAX request (JQuery) for deleting users works from user_list page. It is inside auth/static/auth/ajax_delete_user_from_table.js
- ORM are in auth/model.py, raw SQL in seed fixtures/sql/user_seed.sql
- Seed for DB above. It is loaded with **python init_db.py**
- Here is run process described in README.md
- requirements.txt is provided at the root folder. Additional request was about installation of psycopg2. The answer was that it is already included in SQLAlchemy, but it is not, so it is in requirements.txt
- Comments placed here and there
- Project tested at both Linux and Windows at 2 different machines
- Instuction for venv is provided in README.md. Docker was not used.

Task #2 was not completed.


Author: [Andrew Dybov](mailto:dybov.andrew@gmail.com)
