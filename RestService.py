from typing import Union
import fastapi
from fastapi import FastAPI
import http
from http import HTTPMethod
from http import HTTPStatus
from api import crud
app = FastAPI()





@app.get("/v1/shorts/{id}")
def get_Short(id: int):
    return crud.read_short(id)

@app.get("v1/shorts")
def get_All_Shorts():
    return crud.read_all()

@app.get("/v1/shorts/random")
def get_random_Short():
    return crud.read_short_random()

@app.post("/v1/shorts")
def create_Short(url: str):
    return crud.create_short(url)

@app.delete("/v1/shorts/{id}")
def delete_Short(id: int):
    return crud.delete_short(id)

