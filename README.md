# tagtog-kiss-webhooks

## Requirements

* Python 3.8+ (you can get this with [pyenv](https://github.com/pyenv/pyenv) as in: `pyenv install 3.8.2`)
* [pipenv](https://github.com/pypa/pipenv)

## Install

```shell
# Prepare the virtualenv
pipenv --python $(pyenv which python)
# Enter in the shell
pipenv shell
# Install all dependencies
pipenv sync
```

## Run

```shell
uvicorn main:app --reload
```
