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
pipenv sync  # (or if you are developing: pipenv install)
```

## Run

```shell
uvicorn main:app --reload
# The application will be running on: http://localhost:8000
```

# Endpoints

* http://localhost:8000/will-annotate-document/{username}/{password}

  Where `{username}` and `{password}` are the credentials of the tagtog user making the request. For example, these can be the credentials of the project's owner.
