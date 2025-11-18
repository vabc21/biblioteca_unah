import os
from typing import List

class Settings:
    """Configuración principal de la aplicación - SIN Pydantic Settings"""
    
    # ====== BASE DE DATOS ======
    DB_SERVER: str = os.getenv("DB_SERVER", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 1433))
    DB_NAME: str = os.getenv("DB_NAME", "biblioteca_dev")
    DB_USER: str = os.getenv("DB_USER", "sa")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "YourPassword123!")
    DB_DRIVER: str = os.getenv("DB_DRIVER", "{ODBC Driver 18 for SQL Server}")
    
    # ====== APLICACIÓN ======
    API_TITLE: str = os.getenv("API_TITLE", "Biblioteca API")
    API_VERSION: str = os.getenv("API_VERSION", "1.0.0")
    API_DESCRIPTION: str = os.getenv("API_DESCRIPTION", "API para gestionar una biblioteca con FastAPI y SQL Azure")
    
    # ====== CORS ======
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "*")
    
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
            f"TrustServerCertificate=yes;"
            f"Connection Timeout=30;"
        )
        
        params = urllib.parse.quote_plus(connection_string)
        return f"mssql+pyodbc:///?odbc_connect={params}"
    
    def get_cors_origins(self) -> List[str]:
        """Convertir CORS_ORIGINS a lista"""
        if self.CORS_ORIGINS == "*":
            return ["*"]
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]

# Instancia global de configuración
settings = Settings()