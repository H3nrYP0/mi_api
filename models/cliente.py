from sqlalchemy import Column, Integer, String, Date, Boolean, CheckConstraint
from database import Base

class Cliente(Base):
    __tablename__ = "Cliente"

    id = Column(Integer, primary_key=True, index=True)
    tipoDocumentoID = Column(String(4))
    numero_documento = Column(String(20), nullable=False)
    nombre = Column(String(25), nullable=False)
    apellido = Column(String(20), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero = Column(String(15))
    telefono = Column(String(20))
    correo = Column(String(30))
    municipio = Column(String(15))
    direccion = Column(String(30))
    ocupacion = Column(String(20))
    telefono_emergencia = Column(String(20))
    estado = Column(Boolean, default=True)

    __table_args__ = (
        CheckConstraint("genero IN ('Masculino','Femenino','Otro')", name="ck_cliente_genero"),
    )
