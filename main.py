from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/ping")
@app.get("/")
def ping():
    return "pong"


@app.post("/will-annotate-document", status_code=204)
def will_annotate_document(x_tagtog_webhookid: str = Header(None), x_tagtog_source: str = Header(None), x_tagtog_owner: str = Header(None), x_tagtog_project: str = Header(None), x_tagtog_member: str = Header(None), x_tagtog_docid: str = Header(None), x_tagtog_jobid: str = Header(None)):
    print(x_tagtog_webhookid)
    return
