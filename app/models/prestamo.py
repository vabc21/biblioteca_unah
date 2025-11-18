# app/models/prestamo.py

from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
from datetime import datetime

# ENUM
class EstadoPrestamo:
    ACTIVO = "activo"
    COMPLETADO = "completado"
    VENCIDO = "vencido"

class Prestamo(Base):
    """Modelo para préstamos"""
    __tablename__ = "prestamo"
    
    prestamo_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuario.usuario_id"), nullable=False)
    fecha_prestamo = Column(DateTime, nullable=False, server_default=func.now())
    fecha_devolucion = Column(DateTime, nullable=False)
    estado = Column(String(20), nullable=False, default=EstadoPrestamo.ACTIVO)
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="prestamos")
    detalles = relationship(
        "DetallePrestamo",
        back_populates="prestamo",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<Prestamo {self.prestamo_id}: Usuario {self.usuario_id}>"