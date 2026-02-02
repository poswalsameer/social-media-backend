from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"success": True, "message": "Welcome to the Social Media API"}
