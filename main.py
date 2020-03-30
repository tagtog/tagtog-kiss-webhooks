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
HARDCODED_PASSWORD_FOR_ALL = "yourPassword"


# -----------------------------------------------------------------------------


class Info(BaseModel):
    owner: str
    project: str
    member: str
    webhookid: str
    docid: str
    jobid: str
    format: str = "ann.json"


# -----------------------------------------------------------------------------


def return_empty_annotations():
    return {
        "anncomplete": False,
        "annotatables": [],
        "sources": [],
        "metas": [],
        "entities": [],
        "relations": []
    }


async def success_async_annotate(info: Info):
    logger.info(f"started annotation: {info}")
    await asyncio.sleep(1)  # Wait some time to simulate a real ML prediction
    endpoint = "-api/documents/jobs/v1/success-async-annotate"

    res = requests.post(
        TAGTOG_DOMAIN + endpoint,
        auth=HTTPBasicAuth(info.owner, HARDCODED_PASSWORD_FOR_ALL),
        verify=TAGTOG_SSL_CERTIFICATE,
        params=info,
        json=return_empty_annotations())

    logger.info(f"{res.status_code} {res.text}")
    logger.info("finished")


async def async_annotate(info: Info):
    await success_async_annotate(info)


# -----------------------------------------------------------------------------


@app.get("/ping")
@app.get("/")
async def ping():
    return "pong"


@app.post("/will-annotate-document", status_code=204)
async def will_annotate_document(x_tagtog_webhookid: str = Header(None),
                                 x_tagtog_source: str = Header(None),
                                 x_tagtog_owner: str = Header(None),
                                 x_tagtog_project: str = Header(None),
                                 x_tagtog_member: str = Header(""),
                                 x_tagtog_docid: str = Header(None),
                                 x_tagtog_jobid: str = Header(None)):

    info = Info(
        owner=x_tagtog_owner,
        project=x_tagtog_project,
        member=x_tagtog_member,
        webhookid=x_tagtog_webhookid,
        docid=x_tagtog_docid,
        jobid=x_tagtog_jobid
    )

    logger.info(x_tagtog_webhookid)
    asyncio.create_task(async_annotate(info))

    return
