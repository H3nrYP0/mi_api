from sqlalchemy import Column, Integer, String
from database import Base

class EstadoDeCita(Base):
    __tablename__ = "EstadoDeCita"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(23))
