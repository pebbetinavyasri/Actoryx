from fastapi import FastAPI

app = FastAPI()

@app.get("/greatest/{num1}/{num2}")
def greatest_of_two(num1: int, num2: int):
    if num1 > num2:
        return {"result": f"{num1} is greatest"}
    elif num2 > num1:
        return {"result": f"{num2} is greatest"}
    else:
        return {"result": "Both are equal"}

