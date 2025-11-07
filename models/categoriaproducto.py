from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class CategoriaProducto(Base):
    __tablename__ = "CategoriaProducto"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(15))
    descripcion = Column(String(100))  # corregido nombre de campo
    estado = Column(Boolean, default=True)
