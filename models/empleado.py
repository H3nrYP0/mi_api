from sqlalchemy import Column, Integer, String, Date, Boolean
from database import Base

class Empleado(Base):
    __tablename__ = "Empleado"

    id = Column(Integer, primary_key=True, index=True)
    tipoDocumento = Column(String(4))
    numero_documento = Column(String(20), nullable=False)
    nombre = Column(String(20), nullable=False)
    telefono = Column(String(10))
    direccion = Column(String(30))
    fecha_ingreso = Column(Date, nullable=False)
    cargo = Column(String(10))
    estado = Column(Boolean, default=True)
