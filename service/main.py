import datetime
import requests

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return requests.get(
        "http://mockserver:1080/"
    ).json()