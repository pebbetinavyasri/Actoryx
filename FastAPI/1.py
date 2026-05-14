from fastapi import FastAPI

app = FastAPI()

@app.get("/oddeven/{num}")
def oddeven(num: int):
    if num % 2 == 0:
        return {"result": f"{num} is an even number"}
    else:
        return {"result": f"{num} is an odd number"}
