from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base

class Producto(Base):
    __tablename__ = "Producto"

    id = Column(Integer, primary_key=True, index=True)
    categoriaProductoId = Column(Integer, ForeignKey("CategoriaProducto.id"))
    marcaId = Column(Integer, ForeignKey("Marca.id"))
    nombre = Column(String(20))
    precio_venta = Column(Numeric(10,2))
    precio_compra = Column(Numeric(10,2))
    stock = Column(Integer)
    stock_minimo = Column(Integer)
    descripcion = Column(String(120))
    estado = Column(Boolean, default=True)

    categoria = relationship("CategoriaProducto", backref="productos")
    marca = relationship("Marca", backref="productos")
    imagenes = relationship("Imagenes", back_populates="producto")
    detalle_compra = relationship("DetalleCompra", back_populates="producto")
    detalle_venta = relationship("DetalleVenta", back_populates="producto")
