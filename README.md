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

# Run

```console
python app.py
```
>Note: If in your \*nix OS **python** command is used for python 2 use **python3** instead
>If using **flask run** instead, then do not forget to add environment variable **FLASK_ENV=development**  

# Deploy

Out of scope

Author: [Andrew Dybov](mailto:dybov.andrew@gmail.com)
