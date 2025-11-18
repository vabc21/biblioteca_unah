# app/schemas/prestamo.py

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class DetallePrestamoCreate(BaseModel):
    """Schema para detalle de préstamo al crear"""
    libro_id: int
    estado_ejemplar: str = "bueno"

class PrestamoBase(BaseModel):
    """Schema base para Préstamo"""
    usuario_id: int
    fecha_devolucion: datetime
    estado: str = "activo"

class PrestamoCreate(BaseModel):
    """Schema para crear Préstamo"""
    usuario_id: int
    fecha_devolucion: datetime
    libros: List[DetallePrestamoCreate]

class PrestamoUpdate(BaseModel):
    """Schema para actualizar Préstamo"""
    fecha_devolucion: Optional[datetime] = None
    estado: Optional[str] = None

class PrestamoResponse(PrestamoBase):
    """Schema para respuesta de Préstamo"""
    prestamo_id: int
    fecha_prestamo: datetime
    
    class Config:
        from_attributes = True