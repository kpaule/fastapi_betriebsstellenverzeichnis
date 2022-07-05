from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models
from .database import engine, SessionLocal
from .csv_loader import load_csv

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
load_csv("DBNetz-Betriebsstellenverzeichnis-Stand2021-10.csv")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/api/v1/betriebsstelle")
def fetch_betriebsstelle(rl100_code: str, db: Session = Depends(get_db)):
    betriebsstelle = db.query(models.Betriebsstelle).filter(
        models.Betriebsstelle.rl100_code == rl100_code).first()
    if betriebsstelle:
        return betriebsstelle
    raise HTTPException(status_code=404, detail=f"Die Betriebsstelle mit der Kennung {rl100_code} existiert nicht.")
    
