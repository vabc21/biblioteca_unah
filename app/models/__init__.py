# app/models/__init__.py

from app.models.usuario import Usuario, TipoUsuario, EstadoUsuario
from app.models.categoria import Categoria
from app.models.autor import Autor
from app.models.libro import Libro, LibroAutor, EstadoLibro
from app.models.prestamo import Prestamo, EstadoPrestamo
from app.models.detalle_prestamo import DetallePrestamo, EstadoEjemplar

__all__ = [
    "Usuario",
    "TipoUsuario",
    "EstadoUsuario",
    "Categoria",
    "Autor",
    "Libro",
    "LibroAutor",
    "EstadoLibro",
    "Prestamo",
    "EstadoPrestamo",
    "DetallePrestamo",
    "EstadoEjemplar",
]