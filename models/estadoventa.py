from sqlalchemy import Column, Integer, String
from database import Base

class EstadoVenta(Base):
    __tablename__ = "EstadoVenta"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(23))
