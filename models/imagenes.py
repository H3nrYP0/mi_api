from sqlalchemy import Column, Integer, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Imagenes(Base):
    __tablename__ = "Imagenes"

    id = Column(Integer, primary_key=True, index=True)
    productosId = Column(Integer, ForeignKey("Producto.id"))
    url = Column(Text, nullable=False)

    producto = relationship("Producto", back_populates="imagenes")
