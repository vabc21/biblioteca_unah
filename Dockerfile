FROM python:3.14-slim

WORKDIR /app

# ================================================================
#          Instalar librerías necesarias para pyodbc
# ================================================================

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gnupg2 \
    ca-certificates \
    unixodbc \
    unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && curl https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*

# ================================================================
#            Copiar y instalar dependencias Python
# ================================================================

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ================================================================
#              Copiar código de la aplicación
# ================================================================

COPY . .

# ================================================================
#           Crear usuario no-root por seguridad
# ================================================================

RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# ================================================================
#                  Exponer puerto
# ================================================================

EXPOSE 8000

# ================================================================
#                   Health check
# ================================================================

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# ================================================================
#            Comando para ejecutar la aplicación
# ================================================================

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]