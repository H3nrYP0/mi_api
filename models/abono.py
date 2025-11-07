from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base

class Abono(Base):
    __tablename__ = "Abono"

    id = Column(Integer, primary_key=True, index=True)
    ventaId = Column(Integer, ForeignKey("Venta.id"))
    montoAbonado = Column(Numeric(10,2))

    venta = relationship("Venta")
