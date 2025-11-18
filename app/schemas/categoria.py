# app/schemas/categoria.py

from pydantic import BaseModel, Field
from typing import Optional

class CategoriaBase(BaseModel):
    """Schema base para Categoría"""
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    """Schema para crear Categoría"""
    pass

class CategoriaUpdate(BaseModel):
    """Schema para actualizar Categoría"""
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    descripcion: Optional[str] = None

class CategoriaResponse(CategoriaBase):
    """Schema para respuesta de Categoría"""
    categoria_id: int
    
    class Config:
        from_attributes = True