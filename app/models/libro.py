# app/models/libro.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# ENUM
class EstadoLibro:
    DISPONIBLE = "disponible"
    PRESTADO = "prestado"
    MANTENIMIENTO = "mantenimiento"
    DESCATALOGADO = "descatalogado"

class Libro(Base):
    """Modelo para libros"""
    __tablename__ = "libro"
    
    libro_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(200), nullable=False, index=True)
    editorial = Column(String(100), nullable=True)
    año_publicacion = Column(Integer, nullable=True)
    estado = Column(String(20), nullable=False, default=EstadoLibro.DISPONIBLE)
    categoria_id = Column(Integer, ForeignKey("categoria.categoria_id"), nullable=False)
    
    # Relaciones
    categoria = relationship("Categoria", back_populates="libros")
    autores = relationship(
        "Autor",
        secondary="libro_autor",
        back_populates="libros"
    )
    detalles_prestamo = relationship(
        "DetallePrestamo",
        back_populates="libro",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<Libro {self.libro_id}: {self.titulo}>"

class LibroAutor(Base):
    """Tabla de relación many-to-many entre Libro y Autor"""
    __tablename__ = "libro_autor"
    
    libro_id = Column(Integer, ForeignKey("libro.libro_id"), primary_key=True)
    autor_id = Column(Integer, ForeignKey("autor.autor_id"), primary_key=True)