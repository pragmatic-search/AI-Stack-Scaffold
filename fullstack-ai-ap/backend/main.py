from fastapi import FastAPI
from .routes import ai_model
from .database import connect_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await connect_db()

app.include_router(ai_model.router, prefix="/api")
