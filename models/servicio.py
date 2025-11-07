from sqlalchemy import Column, Integer, String, Numeric, Boolean
from database import Base

class Servicio(Base):
    __tablename__ = "Servicio"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20))
    duracion_min = Column(Integer)
    precio = Column(Numeric(10,2))
    descripcion = Column(String(120))
    estado = Column(Boolean, default=True)
