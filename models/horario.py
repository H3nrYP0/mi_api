from sqlalchemy import Column, Integer, ForeignKey, Time, String
from sqlalchemy.orm import relationship
from database import Base

class Horario(Base):
    __tablename__ = "Horario"

    id = Column(Integer, primary_key=True, index=True)
    empleadoId = Column(Integer, ForeignKey("Empleado.id"))
    horaInicio = Column(Time)
    horaFinal = Column(Time)
    dia = Column(String)

    empleado = relationship("Empleado")
