from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {"root": "http://localhost exists here"}
