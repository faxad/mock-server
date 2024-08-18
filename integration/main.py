import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "source": "integration-service",
        "processed": datetime.datetime.now()
    }