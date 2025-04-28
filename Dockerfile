# Usa una imagen oficial de Python
FROM python:3.12.10-alpine3.20

# Establece el directorio de trabajo
WORKDIR /app

# Instala el cliente de PostgreSQL y dependencias
RUN apk update && apk add --no-cache \
    postgresql-client \
    libpq \
    gcc \
    musl-dev \
    python3-dev

# Copia los archivos del proyecto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expone el puerto en el que Django corre
EXPOSE 8000

# Comando por defecto (puedes usar gunicorn si prefieres)
CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]