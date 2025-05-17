# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo producer.py al contenedor
COPY producer.py .

# Instala la librería confluent-kafka
RUN pip install confluent-kafka

# Comando que se ejecutará al iniciar el contenedor
CMD ["python", "producer.py"]
