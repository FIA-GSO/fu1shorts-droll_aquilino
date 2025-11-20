from typing import Union
import fastapi
from fastapi import FastAPI
import http
from http import HTTPMethod
from http import HTTPStatus
from api import crud
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/getShorts")
def getShorts():
    return crud.read_all()


@app.post("/createShorts")
def createShorts(url: str):
    return crud.create_short(url)
