# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool
from config import settings


# CONFIGURACIÓN DEL ENGINE


engine = create_engine(
    settings.database_url,
    poolclass=NullPool,  # No usar pool con SQL Azure para evitar timeouts
    echo=False,  # Cambiar a True para ver las queries SQL
    connect_args={
        "timeout": 30,
        "check_same_thread": False,
    }
)

# FACTORY DE SESIONES

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# BASE DECLARATIVA

Base = declarative_base()

def get_db():
    """
    Dependencia para obtener sesión de base de datos
    Se usa en los endpoints para inyectar la sesión
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_all_tables():
    """
    Crear todas las tablas en la base de datos
    Se ejecuta al iniciar la aplicación
    """
    Base.metadata.create_all(bind=engine)

def drop_all_tables():
    """
    Eliminar todas las tablas de la base de datos
    ⚠️ SOLO USAR EN DESARROLLO
    """
    Base.metadata.drop_all(bind=engine)