import asyncio
import logging
import time

from fastapi import FastAPI, Header

app = FastAPI()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)-24s %(levelname)-8s %(name)-20s %(message)s"
)

logger = logging.getLogger(__name__)


def annotate():
    return {
        "anncomplete": False,
        "annotatables": [],
        "sources": [],
        "metas": [],
        "entities": [],
        "relations": []
    }


async def success_async_annotate():
    logger.info("started")
    await asyncio.sleep(5)  # Wait some time to simulate a real ML prediction
    logger.info("finished")


# -----------------------------------------------------------------------------


@app.get("/ping")
@app.get("/")
def ping():
    return "pong"


@app.post("/will-annotate-document", status_code=204)
def will_annotate_document(x_tagtog_webhookid: str = Header(None),
                           x_tagtog_source: str = Header(None),
                           x_tagtog_owner: str = Header(None),
                           x_tagtog_project: str = Header(None),
                           x_tagtog_member: str = Header(None),
                           x_tagtog_docid: str = Header(None),
                           x_tagtog_jobid: str = Header(None)):

    logger.info(x_tagtog_webhookid)
    asyncio.run(success_async_annotate())

    return
