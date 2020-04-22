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
pipenv shell  # Unnecessary if you are already in the virtual shell
# export TAGTOG_DOMAIN='https://myOnPremisesTagtogDomain'  # Set this if needed. The default tagtog domain is: https://www.tagtog.net
uvicorn main:app --reload
```

After this, the web server will be running on: http://localhost:8000


# Endpoints

## will-annotate-document

* http://localhost:8000/will-annotate-document/{username}/{password}

  Where `{username}` and `{password}` are the credentials of the tagtog user making the request. For example, these can be the credentials of the project's owner.

### Parameters

* **error**: (optional; default=null) set this value ([url encoded](https://www.urlencoder.org)) with your own error message if you want the server to eventually communicate tagtog of an error in the annotation (that is, call the endpoint `failure-async-annotate`). If you leave this parameter unset, the default is for the server to send some (dummy) annotations to `success-async-annotate`.
* **delaySeconds**: (optional; default=5) delay in seconds for when the server will eventually communicate tagtog of `success-async-annotate`/`failure-async-annotate`
