# Usar una imagen oficial de Python
FROM python:3.9

# Crear el directorio 'crs' dentro del contenedor
WORKDIR /crs

# Copiar todos los archivos dentro del directorio 'crs'
COPY crs/ /crs/

# Instalar dependencias si existe un requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || true

# Definir el comando para ejecutar el script principal
CMD ["python", "app.py"]

#docker build -t mi-app-python .

# Ejecutar el contenedor
#docker run --rm mi-app-python
#docker run --rm -it mi-app-python
