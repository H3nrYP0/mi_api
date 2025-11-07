from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint
from database import Base

class Proveedor(Base):
    __tablename__ = "Proveedor"

    id = Column(Integer, primary_key=True, index=True)
    tipo_proveedor = Column(String(20))  # enforce via check constraint if desired
    tipoDeDocumento = Column(String(4))
    documento = Column(String(20))
    razon_social_o_Nombre = Column(String(30))
    Contacto = Column(String(20))
    telefono = Column(String(10))
    correo = Column(String(50))
    departamento = Column(String(15))
    municipio = Column(String(15))
    direccion = Column(String(30))
    estado = Column(Boolean, default=True)

    __table_args__ = (
        CheckConstraint("tipo_proveedor IN ('Persona Natural','Persona Jurídica')", name="ck_proveedor_tipo"),
    )
