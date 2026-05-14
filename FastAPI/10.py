from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PrimeNumber(BaseModel):
    num: int


# GET Method
@app.get("/")
def check_prime_get(num: int):

    if num <= 1:
        result = "Not Prime"
    else:
        result = "Prime"
        for i in range(2, num):
            if num % i == 0:
                result = "Not Prime"
                break

    return {
        "Method": "GET",
        "Number": num,
        "Result": result
    }


# POST Method
@app.post("/")
def check_prime_post(data: PrimeNumber):

    num = data.num

    if num <= 1:
        result = "Not Prime"
    else:
        result = "Prime"
        for i in range(2, num):
            if num % i == 0:
                result = "Not Prime"
                break

    return {
        "Method": "POST",
        "Number": num,
        "Result": result
    }