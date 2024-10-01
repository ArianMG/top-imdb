# Dockerfile

FROM python:3.12

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY ./python /app/python
COPY ./cmd /app/cmd
COPY ./LEEME.md /app/LEEME.md
COPY ./aclImdb /app/aclImdb

# Instalar Poetry
RUN pip install poetry

# Instalar dependencias del proyecto
RUN cd python && poetry install

# Establecer los volúmenes para persistencia
VOLUME ["/app/python", "/app/cmd"]

# Comando por defecto al iniciar el contenedor
CMD ["bash"]

