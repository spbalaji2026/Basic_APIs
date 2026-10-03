
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CalculatorInput(BaseModel):
    a: float
    b: float
    operation: str


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Calculator API"}


@app.post("/calculate")
def calculate(data: CalculatorInput):

    if data.operation == "add":
        result = data.a + data.b

    elif data.operation == "subtract":
        result = data.a - data.b

    elif data.operation == "multiply":
        result = data.a * data.b

    elif data.operation == "divide":
        if data.b == 0:
            return {"error": "Cannot divide by zero"}
        result = data.a / data.b

    else:
        return {
            "error": "Invalid operation",
            "allowed_operations": [
                "add", "subtract", "multiply", "divide"
            ]
        }

    return {
        "a": data.a,
        "b": data.b,
        "operation": data.operation,
        "result": result
    }