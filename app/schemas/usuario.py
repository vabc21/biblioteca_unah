# app/schemas/usuario.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    """Schema base para Usuario"""
    nombre: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    telefono: Optional[str] = Field(None, max_length=15)
    tipo: str = "estudiante"
    estado: str = "activo"

class UsuarioCreate(UsuarioBase):
    """Schema para crear Usuario"""
    pass

class UsuarioUpdate(BaseModel):
    """Schema para actualizar Usuario"""
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, max_length=15)
    tipo: Optional[str] = None
    estado: Optional[str] = None

class UsuarioResponse(UsuarioBase):
    """Schema para respuesta de Usuario"""
    usuario_id: int
    fecha_registro: datetime
    
    class Config:
        from_attributes = True