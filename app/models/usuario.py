# app/models/usuario.py

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
from datetime import datetime

class TipoUsuario:
    ESTUDIANTE = "estudiante"
    PROFESOR = "profesor"
    BIBLIOTECA = "biblioteca"

class EstadoUsuario:
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    SUSPENDIDO = "suspendido"

class Usuario(Base):
    """Modelo para usuarios del sistema"""
    __tablename__ = "usuario"
    
    usuario_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    telefono = Column(String(15), nullable=True)
    tipo = Column(String(20), nullable=False, default=TipoUsuario.ESTUDIANTE)
    estado = Column(String(20), nullable=False, default=EstadoUsuario.ACTIVO)
    fecha_registro = Column(DateTime, nullable=False, server_default=func.now())
    
    # Relaciones
    prestamos = relationship("Prestamo", back_populates="usuario", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Usuario {self.usuario_id}: {self.nombre}>"
