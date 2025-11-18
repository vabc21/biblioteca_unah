# app/models/detalle_prestamo.py

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base

class EstadoEjemplar:
    BUENO = "bueno"
    DAÑADO = "dañado"
    EXTRAVIADO = "extraviado"

class DetallePrestamo(Base):
    """Modelo para detalles de préstamo (libros en un préstamo)"""
    __tablename__ = "detalle_prestamo"
    
    detalle_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    prestamo_id = Column(Integer, ForeignKey("prestamo.prestamo_id"), nullable=False)
    libro_id = Column(Integer, ForeignKey("libro.libro_id"), nullable=False)
    estado_ejemplar = Column(String(20), nullable=False, default=EstadoEjemplar.BUENO)
    
    # Relaciones
    prestamo = relationship("Prestamo", back_populates="detalles")
    libro = relationship("Libro", back_populates="detalles_prestamo")
    
    def __repr__(self):
        return f"<DetallePrestamo {self.detalle_id}: Préstamo {self.prestamo_id}>"