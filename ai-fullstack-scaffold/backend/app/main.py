from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .auth import get_password_hash, verify_password
from .models import User
from .database import SessionLocal
from .inference import generate_text
from .model_utils import validate_prompt
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(password)
    db_user = User(email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    return {"message": "User created"}

@app.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Logged in"}

@app.post("/predict")
def predict(prompt: str):
    try:
        validate_prompt(prompt)
        result = generate_text(prompt)
        return {"response": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

from .kafka_consumer import stream_logs
from .dashboard_data import generate_summary

@app.get("/dashboard")
def dashboard():
    # Collect only the first 10 messages to avoid long delay
    logs = []
    for i, log in enumerate(stream_logs()):
        logs.append(log)
        if i >= 9: break
    summary = generate_summary(logs)
    return summary
