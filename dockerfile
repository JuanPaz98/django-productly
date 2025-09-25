# Imagen base de Python 3.13 (slim para reducir peso)
FROM python:3.13.2-slim

# Variables de entorno recomendadas
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar los requirements
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Crear directorio para archivos estáticos
RUN mkdir -p /app/staticfiles

# Ejecutar migraciones y recopilar archivos estáticos
RUN python manage.py migrate --noinput || echo "Migrations failed, continuing..."
RUN python manage.py collectstatic --noinput

# Crear un script de inicio
RUN echo '#!/bin/bash\n\
    python manage.py migrate --noinput\n\
    python manage.py collectstatic --noinput\n\
    exec gunicorn --bind 0.0.0.0:8000 productly.wsgi:application --workers=3 --timeout=60 --log-level=info' > /app/start.sh

RUN chmod +x /app/start.sh

# Exponer el puerto
EXPOSE 8000

# Usar el script de inicio
CMD ["/app/start.sh"]