# app/schemas/libro.py

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class LibroBase(BaseModel):
    """Schema base para Libro"""
    titulo: str = Field(..., min_length=1, max_length=200)
    editorial: Optional[str] = Field(None, max_length=100)
    año_publicacion: Optional[int] = None
    estado: str = "disponible"
    categoria_id: int

class LibroCreate(LibroBase):
    """Schema para crear Libro"""
    autores_ids: Optional[List[int]] = []

class LibroUpdate(BaseModel):
    """Schema para actualizar Libro"""
    titulo: Optional[str] = Field(None, min_length=1, max_length=200)
    editorial: Optional[str] = None
    año_publicacion: Optional[int] = None
    estado: Optional[str] = None
    categoria_id: Optional[int] = None
    autores_ids: Optional[List[int]] = None

class LibroResponse(LibroBase):
    """Schema para respuesta de Libro"""
    libro_id: int
    
    class Config:
        from_attributes = True