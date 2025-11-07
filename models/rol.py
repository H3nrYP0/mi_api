from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Rol(Base):
    __tablename__ = "Rol"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(25))
    descripcion = Column(String(60))
    estado = Column(Boolean, default=True)

    usuarios = relationship("Usuario", back_populates="rol")
