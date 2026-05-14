from fastapi import FastAPI

app = FastAPI()

@app.get("/checksign/{num}")
def check_sign(num: int):
    if num > 0:
        return {"result": f"{num} is Positive number"}
    elif num < 0:
        return {"result": f"{num} is Negative number"}
    else:
        return {"result": "Zero"}

