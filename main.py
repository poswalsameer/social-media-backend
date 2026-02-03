from fastapi import FastAPI
from sqlmodel import SQLModel
from db.main import engine

import models

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


@app.get("/")
def root():
    return {"status": "connected"}
