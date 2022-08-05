# Floriza


## Update Python

```bash
python -m pip install --upgrade pip
python -m pip install --upgrade wheel
python -m pip install --upgrade setuptools
python -m pip install --upgrade virtualenv
```

## Create a virtual environment

```bash
cd /path/to/project
```

### WINDOWS

```bash
Set-ExecutionPolicy Unrestricted -Scope Process
python -m venv .env

* Activate It
.\.venv\Scripts\activate
```

### LINUX

```bash
python -m venv .venv
source .venv/bin/activate
```

## Install packages

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run Application
```bash
flask run
```