from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class DetalleCompra(Base):
    __tablename__ = "DetalleCompra"

    id = Column(Integer, primary_key=True, index=True)
    compraId = Column(Integer, ForeignKey("Compra.id"))
    productoId = Column(Integer, ForeignKey("Producto.id"))
    precioUnidad = Column(Numeric(10,2))
    cantidad = Column(Integer)
    subtotal = Column(Numeric(10,2))

    compra = relationship("Compra", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalle_compra")
