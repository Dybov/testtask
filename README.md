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

To run:
```console
python app.py
```
>Note: If in your \*nix OS **python** command is used for python 2 use **python3** instead
>If using **flask run** instead, then do not forget to add environment variable **FLASK_ENV=development**  

After adding **project_folder/config/prod.py** file with **ProdConfig** class it will run using that config.

# Deploy

Out of scope of the task.

Author: [Andrew Dybov](mailto:dybov.andrew@gmail.com)
