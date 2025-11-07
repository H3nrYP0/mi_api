from sqlalchemy import Column, Integer, ForeignKey, String, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

class HistorialDeFormula(Base):
    __tablename__ = "HistorialDeFormula"

    id = Column(Integer, primary_key=True, index=True)
    clienteId = Column(Integer, ForeignKey("Cliente.id"))
    descripcion = Column(String(100))
    OD_Esfera = Column(String(20))
    OD_Cilindro = Column(String(20))
    OD_Eje = Column(String(20))
    OI_Esfera = Column(String(20))
    OI_Cilindro = Column(String(20))
    OI_Eje = Column(String(20))
    fecha = Column(TIMESTAMP)

    cliente = relationship("Cliente")
