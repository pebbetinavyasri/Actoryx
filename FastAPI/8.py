from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Request body model
class TableNumber(BaseModel):
    n: int


# GET Method
@app.get("/")
def multiplication_table_get(n: int):

    table = []

    for i in range(1, 11):
        table.append(f"{n} x {i} = {n * i}")

    return {
        "Method": "GET",
        "Table": table
    }


# POST Method
@app.post("/")
def multiplication_table_post(data: TableNumber):

    table = []

    for i in range(1, 11):
        table.append(f"{data.n} x {i} = {data.n * i}")

    return {
        "Method": "POST",
        "Table": table
    }