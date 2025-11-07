from sqlalchemy import Column, Integer, ForeignKey, Numeric, TIMESTAMP, String
from sqlalchemy.orm import relationship
from database import Base

class Venta(Base):
    __tablename__ = "Venta"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("Cliente.id"))
    estadoDeVentaId = Column(Integer, ForeignKey("EstadoVenta.id"))
    citaId = Column(Integer, ForeignKey("Cita.id"))
    empleadoId = Column(Integer, ForeignKey("Empleado.id"))
    metodo_pago = Column(String(50))
    fecha = Column(TIMESTAMP)
    totalVenta = Column(Numeric(10,2))

    cliente = relationship("Cliente")
    estado = relationship("EstadoVenta")
    cita = relationship("Cita")
