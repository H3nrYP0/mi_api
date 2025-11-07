from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal

app = FastAPI()

# Crear tablas automáticamente (solo temporal mientras desarrollamos)
Base.metadata.create_all(bind=engine)

# Dependencia de BD para usar en endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API funcionando correctamente con PostgreSQL ✅"}
