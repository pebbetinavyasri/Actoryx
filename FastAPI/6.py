from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Request body model
class Numbers(BaseModel):
    a: float
    b: float


# GET Method
@app.get("/")
def calculator_get(a: float, b: float):

    division = a / b if b != 0 else "Undefined"

    return {
        "Method": "GET",
        "Addition": a + b,
        "Subtraction": a - b,
        "Multiplication": a * b,
        "Division": division
    }


# POST Method
@app.post("/")
def calculator_post(numbers: Numbers):

    a = numbers.a
    b = numbers.b

    division = a / b if b != 0 else "Undefined"

    return {
        "Method": "POST",
        "Addition": a + b,
        "Subtraction": a - b,
        "Multiplication": a * b,
        "Division": division
    }