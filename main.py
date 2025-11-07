from fastapi import FastAPI
from sqlalchemy import inspect
from database import engine

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando con PostgreSQL ✅"}

@app.get("/tablas")
def mostrar_tablas():
    inspector = inspect(engine)
    tablas = inspector.get_table_names()
    return {"tablas": tablas}
