from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "Usuario"

    id = Column(Integer, primary_key=True, index=True)
    rol_id = Column(Integer, ForeignKey("Rol.id"))
    nombre = Column(String(25), nullable=False)
    correo = Column(String(27), nullable=False)
    contrasenia = Column(String, nullable=False)
    estado = Column(Boolean, default=True)

    rol = relationship("Rol", back_populates="usuarios")
