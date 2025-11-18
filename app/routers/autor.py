# app/routers/autor.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app.models.autor import Autor
from app.schemas.autor import AutorCreate, AutorUpdate, AutorResponse

router = APIRouter(prefix="/autores", tags=["Autores"])

@router.post("", response_model=AutorResponse, status_code=status.HTTP_201_CREATED)
def crear_autor(autor: AutorCreate, db: Session = Depends(get_db)):
    """Crear un nuevo autor"""
    db_autor = Autor(**autor.dict())
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor

@router.get("", response_model=list[AutorResponse])
def listar_autores(db: Session = Depends(get_db)):
    """Listar todos los autores"""
    return db.query(Autor).all()

@router.get("/{autor_id}", response_model=AutorResponse)
def obtener_autor(autor_id: int, db: Session = Depends(get_db)):
    """Obtener autor por ID"""
    autor = db.query(Autor).filter(Autor.autor_id == autor_id).first()
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return autor

@router.put("/{autor_id}", response_model=AutorResponse)
def actualizar_autor(autor_id: int, autor_update: AutorUpdate, db: Session = Depends(get_db)):
    """Actualizar autor"""
    autor = db.query(Autor).filter(Autor.autor_id == autor_id).first()
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    
    for key, value in autor_update.dict(exclude_unset=True).items():
        setattr(autor, key, value)
    db.commit()
    db.refresh(autor)
    return autor

@router.delete("/{autor_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_autor(autor_id: int, db: Session = Depends(get_db)):
    """Eliminar autor"""
    autor = db.query(Autor).filter(Autor.autor_id == autor_id).first()
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    db.delete(autor)
    db.commit()