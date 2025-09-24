# Imagen base de Python 3.13 (slim para reducir peso)
FROM python:3.13.2-slim

# Variables de entorno recomendadas
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema (ejemplo: PostgreSQL client, gcc, etc.)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar los requirements
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Copiar el resto del proyecto
COPY . .

# Compila todos los assets en app/staticfiles
RUN python manage.py collectstatic --noinput

# Exponer el puerto de Django (gunicorn correrá aquí)
EXPOSE 8000

# Comando por defecto (gunicorn recomendado en producción)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "productly.wsgi:application", "--workers=3", "--timeout=60"]


