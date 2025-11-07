from sqlalchemy import Column, Integer, Numeric, ForeignKey, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Compra(Base):
    __tablename__ = "Compra"

    id = Column(Integer, primary_key=True, index=True)
    proveedorId = Column(Integer, ForeignKey("Proveedor.id"))
    total = Column(Numeric(10,2))
    fecha = Column(TIMESTAMP)
    estadoCompra = Column(Boolean)

    proveedor = relationship("Proveedor", backref="compras")
    detalles = relationship("DetalleCompra", back_populates="compra")
