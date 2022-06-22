import app.fibonacci as fib
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def root():
    return {"massage": "Plese enter a positive integer between 0 and 100 -> /input/int"}

@app.get("/input/{n}")
async def get_n(n: int):
    output_seq = fib.fibo_seq(n)
    return {"fibonacci sequence:": output_seq}
