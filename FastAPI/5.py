from fastapi import FastAPI

app = FastAPI()

@app.get("/arithmetic/{num1}/{num2}")
def arithmetic_operations(num1: int, num2: int):
    result = {
        "Addition": num1 + num2,
        "Subtraction": num1 - num2,
        "Multiplication": num1 * num2
    }

    if num2 != 0:
        result["Division"] = num1 / num2
        result["Modular"] = num1 % num2
    else:
        result["Message"] = "Division and Modular by zero is not allowed"

    return result