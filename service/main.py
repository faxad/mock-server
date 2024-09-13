import datetime
import requests

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    token = request.headers.get('X-Token')
    return requests.get(
        "http://mockserver:1080/",
        headers={"X-Token":token}
    ).json()