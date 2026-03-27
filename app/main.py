from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Hello local docker"}


@app.get("/hello")
def hello():
    return { "msg": "Hello fredde"}