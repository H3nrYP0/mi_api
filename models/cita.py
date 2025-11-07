from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Time, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base

class Cita(Base):
    __tablename__ = "Cita"

    id = Column(Integer, primary_key=True, index=True)
    clienteId = Column(Integer, ForeignKey("Cliente.id"))
    servicioId = Column(Integer, ForeignKey("Servicio.id"))
    empleadoId = Column(Integer, ForeignKey("Empleado.id"))
    metodo_pago = Column(String(20))
    hora = Column(Time)   # hora en tipo TIME
    duracion = Column(Integer)
    fecha = Column(TIMESTAMP)
    estadoDeCitaId = Column(Integer, ForeignKey("EstadoDeCita.id"))

    cliente = relationship("Cliente")
    servicio = relationship("Servicio")
    empleado = relationship("Empleado")
    estado = relationship("EstadoDeCita")
    __table_args__ = (
        CheckConstraint("metodo_pago IN ('Efectivo','Tarjeta','Transferencia')", name="ck_cita_metodo"),
    )
