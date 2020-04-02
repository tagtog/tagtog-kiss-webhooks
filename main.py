import asyncio
import logging
# import json
from pydantic import BaseModel
import requests
from requests.auth import HTTPBasicAuth
from fastapi import FastAPI, Header

app = FastAPI()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)-24s %(levelname)-8s %(name)-20s %(message)s"
)

logger = logging.getLogger(__name__)


# -----------------------------------------------------------------------------


TAGTOG_DOMAIN = "https://localhost:9443/"
TAGTOG_SSL_CERTIFICATE = False


# -----------------------------------------------------------------------------


class AsyncAnnotateParams(BaseModel):
    owner: str
    project: str
    member: str
    webhookid: str
    docid: str
    jobid: str
    format: str = None


# -----------------------------------------------------------------------------


def return_empty_annotations():
    return {
        "anncomplete": False,
        "annotatables": [],
        "sources": [],
        "metas": {},
        "entities": [],
        "relations": []
    }


async def success_async_annotate(username: str, password: str, info: AsyncAnnotateParams):
    logger.info(f"start success_async_annotate: {info}")
    await asyncio.sleep(5)  # Wait some time to simulate a real ML prediction
    endpoint = "-api/documents/jobs/v1/success-async-annotate"

    res = requests.post(
        TAGTOG_DOMAIN + endpoint,
        auth=HTTPBasicAuth(username, password),
        verify=TAGTOG_SSL_CERTIFICATE,
        params=info,
        json=return_empty_annotations())

    logger.info(f"end success_async_annotate: {res.status_code} {res.text}")


async def failure_async_annotate(username: str, password: str, info: AsyncAnnotateParams, error: str):
    logger.info(f"start failure_async_annotate: {info}")
    await asyncio.sleep(5)  # Wait some time to simulate a real ML prediction with error
    endpoint = "-api/documents/jobs/v1/failure-async-annotate"

    res = requests.post(
        TAGTOG_DOMAIN + endpoint,
        auth=HTTPBasicAuth(username, password),
        verify=TAGTOG_SSL_CERTIFICATE,
        params=info,
        data=error)

    logger.info(f"end failure_async_annotate: {res.status_code} {res.text}")


async def async_annotate(username: str, password: str, info: AsyncAnnotateParams, error: str = None):
    if error:
        info.format = "error"
        await failure_async_annotate(username, password, info, error)
    else:
        info.format = "ann.json"
        await success_async_annotate(username, password, info)


# -----------------------------------------------------------------------------


@app.get("/ping")
@app.get("/")
async def ping():
    return "pong"


@app.post("/will-annotate-document/{username}/{password}", status_code=204)
async def will_annotate_document(
        username: str,
        password: str,
        # Optional query parameter.
        # If not given, our server will respond with "success-async-annotate"
        # otherwise, our server will respond with "failure-async-annotate" returning the error string given
        error: str = None,
        x_tagtog_webhookid: str = Header(None),
        x_tagtog_source: str = Header(None),
        x_tagtog_owner: str = Header(None),
        x_tagtog_project: str = Header(None),
        x_tagtog_member: str = Header(""),
        x_tagtog_docid: str = Header(None),
        x_tagtog_jobid: str = Header(None)):

    info = AsyncAnnotateParams(
        owner=x_tagtog_owner,
        project=x_tagtog_project,
        member=x_tagtog_member,
        webhookid=x_tagtog_webhookid,
        docid=x_tagtog_docid,
        jobid=x_tagtog_jobid
    )

    logger.info(f"will_annotate_document: {info}")
    asyncio.create_task(async_annotate(username, password, info, error))

    return
