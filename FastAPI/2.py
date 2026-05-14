from fastapi import FastAPI

app = FastAPI()

@app.get("/checkvote/{age}")
def checkvote(age: int):
    if age >= 18:
        return {"result": "Eligible to vote"}
    else:
        return {"result": "Not Eligible to vote"}
