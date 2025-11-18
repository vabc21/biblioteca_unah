# app/routers/__init__.py

from fastapi import APIRouter
from app.routers import usuario, categoria, autor, libro, prestamo

router = APIRouter(prefix="/api/v1")

router.include_router(usuario.router)
router.include_router(categoria.router)
router.include_router(autor.router)
router.include_router(libro.router)
router.include_router(prestamo.router)

__all__ = ["router"]
