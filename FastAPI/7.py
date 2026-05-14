from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Request body model
class NaturalNumber(BaseModel):
    num: int


# GET Method
@app.get("/nnatural")
def n_natural_numbers_get(num: int):

    numbers = []

    for i in range(1, num + 1):
        numbers.append(i)

    return {
        "Method": "GET",
        "First n Natural Numbers": numbers
    }


# POST Method
@app.post("/nnatural")
def n_natural_numbers_post(data: NaturalNumber):

    numbers = []

    for i in range(1, data.num + 1):
        numbers.append(i)

    return {
        "Method": "POST",
        "First n Natural Numbers": numbers
    }