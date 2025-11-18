# app/schemas/__init__.py

from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.schemas.categoria import CategoriaCreate, CategoriaUpdate, CategoriaResponse
from app.schemas.autor import AutorCreate, AutorUpdate, AutorResponse
from app.schemas.libro import LibroCreate, LibroUpdate, LibroResponse
from app.schemas.prestamo import PrestamoCreate, PrestamoUpdate, PrestamoResponse, DetallePrestamoCreate

__all__ = [
    "UsuarioCreate",
    "UsuarioUpdate",
    "UsuarioResponse",
    "CategoriaCreate",
    "CategoriaUpdate",
    "CategoriaResponse",
    "AutorCreate",
    "AutorUpdate",
    "AutorResponse",
    "LibroCreate",
    "LibroUpdate",
    "LibroResponse",
    "PrestamoCreate",
    "PrestamoUpdate",
    "PrestamoResponse",
    "DetallePrestamoCreate",
]