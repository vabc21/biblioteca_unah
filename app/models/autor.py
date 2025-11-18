# app/models/autor.py

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base
from datetime import date

class Autor(Base):
    """Modelo para autores"""
    __tablename__ = "autor"
    
    autor_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, index=True)
    nacionalidad = Column(String(50), nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)
    
    # Relaciones (many-to-many through libro_autor)
    libros = relationship(
        "Libro",
        secondary="libro_autor",
        back_populates="autores"
    )
    
    def __repr__(self):
        return f"<Autor {self.autor_id}: {self.nombre}>"