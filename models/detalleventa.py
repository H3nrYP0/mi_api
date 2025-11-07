from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base

class DetalleVenta(Base):
    __tablename__ = "DetalleVenta"

    id = Column(Integer, primary_key=True, index=True)
    productoId = Column(Integer, ForeignKey("Producto.id"))
    VentaId = Column(Integer, ForeignKey("Venta.id"))
    cantidad = Column(Integer)
    precioUnitario = Column(Numeric(10,2))
    descuento = Column(Numeric(5,2))
    subtotal = Column(Numeric(10,2))

    producto = relationship("Producto", back_populates="detalle_venta")
    venta = relationship("Venta")
