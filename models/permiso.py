from sqlalchemy import Column, Integer, String
from database import Base

class Permiso(Base):
    __tablename__ = "Permiso"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(23))
