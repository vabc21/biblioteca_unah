# app/routers/prestamo.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app.models.prestamo import Prestamo
from app.models.detalle_prestamo import DetallePrestamo
from app.schemas.prestamo import PrestamoCreate, PrestamoUpdate, PrestamoResponse

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])

@router.post("", response_model=PrestamoResponse, status_code=status.HTTP_201_CREATED)
def crear_prestamo(prestamo: PrestamoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo préstamo"""
    db_prestamo = Prestamo(
        usuario_id=prestamo.usuario_id,
        fecha_devolucion=prestamo.fecha_devolucion
    )
    
    for detalle in prestamo.libros:
        db_detalle = DetallePrestamo(
            libro_id=detalle.libro_id,
            estado_ejemplar=detalle.estado_ejemplar
        )
        db_prestamo.detalles.append(db_detalle)
    
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

@router.get("", response_model=list[PrestamoResponse])
def listar_prestamos(db: Session = Depends(get_db)):
    """Listar todos los préstamos"""
    return db.query(Prestamo).all()

@router.get("/{prestamo_id}", response_model=PrestamoResponse)
def obtener_prestamo(prestamo_id: int, db: Session = Depends(get_db)):
    """Obtener préstamo por ID"""
    prestamo = db.query(Prestamo).filter(Prestamo.prestamo_id == prestamo_id).first()
    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return prestamo

@router.put("/{prestamo_id}", response_model=PrestamoResponse)
def actualizar_prestamo(prestamo_id: int, prestamo_update: PrestamoUpdate, db: Session = Depends(get_db)):
    """Actualizar préstamo"""
    prestamo = db.query(Prestamo).filter(Prestamo.prestamo_id == prestamo_id).first()
    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    
    for key, value in prestamo_update.dict(exclude_unset=True).items():
        setattr(prestamo, key, value)
    db.commit()
    db.refresh(prestamo)
    return prestamo

@router.delete("/{prestamo_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_prestamo(prestamo_id: int, db: Session = Depends(get_db)):
    """Eliminar préstamo"""
    prestamo = db.query(Prestamo).filter(Prestamo.prestamo_id == prestamo_id).first()
    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    db.delete(prestamo)
    db.commit()

@router.get("/usuario/{usuario_id}", response_model=list[PrestamoResponse])
def obtener_prestamos_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Obtener todos los préstamos de un usuario"""
    prestamos = db.query(Prestamo).filter(Prestamo.usuario_id == usuario_id).all()
    if not prestamos:
        raise HTTPException(status_code=404, detail="No hay préstamos para este usuario")
    return prestamos