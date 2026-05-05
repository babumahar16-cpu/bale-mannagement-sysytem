from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Controller Running"}

@app.get("/predict")
def predict(value: float):
    return {"output": value * 2}
