# config.py

from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """Configuración principal de la aplicación"""
    
    # ====== BASE DE DATOS ======
    DB_SERVER: str
    DB_PORT: int = 1433
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_DRIVER: str = "{ODBC Driver 18 for SQL Server}"
    
    # ====== APLICACIÓN ======
    API_TITLE: str = "Biblioteca API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "API para gestionar una biblioteca con FastAPI y SQL Azure"
    
    # ====== CORS ======
    CORS_ORIGINS: List[str] = ["*"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
    @property
    def database_url(self) -> str:
        """
        Construir la URL de conexión a Azure SQL Database
        Formato: mssql+pyodbc:///?odbc_connect={connection_string}
        """
        import urllib.parse
        
        connection_string = (
            f"Driver={self.DB_DRIVER};"
            f"Server=tcp:{self.DB_SERVER},{self.DB_PORT};"
            f"Database={self.DB_NAME};"
            f"Uid={self.DB_USER};"
            f"Pwd={self.DB_PASSWORD};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=no;"
            f"Connection Timeout=30;"
        )
        
        params = urllib.parse.quote_plus(connection_string)
        return f"mssql+pyodbc:///?odbc_connect={params}"

# Instancia global de configuración
settings = Settings()