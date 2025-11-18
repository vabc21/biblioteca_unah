# app/dependencies.py

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db

async def verify_database_connection(db: Session = Depends(get_db)):
    """Verifica que la conexión a la base de datos esté disponible"""
    try:
        db.execute("SELECT 1")
        return db
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Base de datos no disponible"
        )