from fastapi import FastAPI
import models

app = FastAPI()

def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()
