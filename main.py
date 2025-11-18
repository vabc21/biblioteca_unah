# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from config import settings
from database import create_all_tables
from app.routers import router

# ================================================================
#                     LIFESPAN EVENTS
# ================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Eventos de ciclo de vida de la aplicación
    - Startup: Se ejecuta al iniciar
    - Shutdown: Se ejecuta al cerrar
    """
    # ====== STARTUP ======
    print("=" * 50)
    print("🚀 Iniciando aplicación...")
    print("=" * 50)
    
    # Crear tablas si no existen
    create_all_tables()
    print("✅ Tablas de base de datos verificadas/creadas")
    print("=" * 50)
    
    yield
    
    # ====== SHUTDOWN ======
    print("=" * 50)
    print("🔴 Cerrando aplicación...")
    print("=" * 50)

# ================================================================
#                   CREAR APLICACIÓN FASTAPI
# ================================================================

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    lifespan=lifespan
)

# ================================================================
#                      MIDDLEWARES
# ================================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================================================================
#                   INCLUIR ROUTERS
# ================================================================

app.include_router(router, prefix="/api/v1")

# ================================================================
#                     ENDPOINTS BASE
# ================================================================

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": settings.API_TITLE,
        "version": settings.API_VERSION
    }

@app.get("/", tags=["Root"])
def root():
    """Endpoint raíz"""
    return {
        "message": f"Bienvenido a {settings.API_TITLE}",
        "version": settings.API_VERSION,
        "documentation": "/docs",
        "redoc": "/redoc"
    }

# ================================================================
#                   PUNTO DE ENTRADA
# ================================================================

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )