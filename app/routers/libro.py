# app/routers/libro.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db
from app.models.libro import Libro
from app.models.autor import Autor
from app.schemas.libro import LibroCreate, LibroUpdate, LibroResponse

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("", response_model=LibroResponse, status_code=status.HTTP_201_CREATED)
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    """Crear un nuevo libro"""
    db_libro = Libro(**libro.dict(exclude={"autores_ids"}))
    
    if libro.autores_ids:
        autores = db.query(Autor).filter(Autor.autor_id.in_(libro.autores_ids)).all()
        db_libro.autores.extend(autores)
    
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro

@router.get("", response_model=list[LibroResponse])
def listar_libros(db: Session = Depends(get_db)):
    """Listar todos los libros"""
    return db.query(Libro).all()

@router.get("/{libro_id}", response_model=LibroResponse)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    """Obtener libro por ID"""
    libro = db.query(Libro).filter(Libro.libro_id == libro_id).first()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

@router.put("/{libro_id}", response_model=LibroResponse)
def actualizar_libro(libro_id: int, libro_update: LibroUpdate, db: Session = Depends(get_db)):
    """Actualizar libro"""
    libro = db.query(Libro).filter(Libro.libro_id == libro_id).first()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
    update_data = libro_update.dict(exclude_unset=True, exclude={"autores_ids"})
    for key, value in update_data.items():
        setattr(libro, key, value)
    
    if libro_update.autores_ids is not None:
        libro.autores.clear()
        if libro_update.autores_ids:
            autores = db.query(Autor).filter(Autor.autor_id.in_(libro_update.autores_ids)).all()
            libro.autores.extend(autores)
    
    db.commit()
    db.refresh(libro)
    return libro

@router.delete("/{libro_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    """Eliminar libro"""
    libro = db.query(Libro).filter(Libro.libro_id == libro_id).first()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    db.delete(libro)
    db.commit()