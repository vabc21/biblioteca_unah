# app/schemas/autor.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class AutorBase(BaseModel):
    """Schema base para Autor"""
    nombre: str = Field(..., min_length=1, max_length=100)
    nacionalidad: Optional[str] = Field(None, max_length=50)
    fecha_nacimiento: Optional[date] = None

class AutorCreate(AutorBase):
    """Schema para crear Autor"""
    pass

class AutorUpdate(BaseModel):
    """Schema para actualizar Autor"""
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    nacionalidad: Optional[str] = None
    fecha_nacimiento: Optional[date] = None

class AutorResponse(AutorBase):
    """Schema para respuesta de Autor"""
    autor_id: int
    
    class Config:
        from_attributes = True