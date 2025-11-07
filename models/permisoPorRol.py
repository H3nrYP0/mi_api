from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class permisoPorRol(Base):
    __tablename__ = "permisoPorRol"

    id = Column(Integer, primary_key=True, index=True)
    rolId = Column(Integer, ForeignKey("Rol.id"))
    permisoId = Column(Integer, ForeignKey("Permiso.id"))

    rol = relationship("Rol")
    permiso = relationship("Permiso")
