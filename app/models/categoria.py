# app/models/categoria.py

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    """Modelo para categorías de libros"""
    __tablename__ = "categoria"
    
    categoria_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True, index=True)
    descripcion = Column(Text, nullable=True)
    
    # Relaciones
    libros = relationship("Libro", back_populates="categoria", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Categoria {self.categoria_id}: {self.nombre}>"