from fastapi import FastAPI

app = FastAPI()


# GET Method
@app.get("/")
def table_of_9_get():

    table = []

    for i in range(1, 11):
        table.append(f"9 x {i} = {9 * i}")

    return {
        "Method": "GET",
        "Table": table
    }


# POST Method
@app.post("/")
def table_of_9_post():

    table = []

    for i in range(1, 11):
        table.append(f"9 x {i} = {9 * i}")

    return {
        "Method": "POST",
        "Table": table
    }