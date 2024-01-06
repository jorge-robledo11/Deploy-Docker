# Usar una imagen base de Miniconda. Esta imagen incluye Conda, un sistema de gestión de paquetes y entornos.
FROM continuumio/miniconda3

# Establecer el directorio de trabajo en el contenedor a /app.
WORKDIR /app

# Copiar los archivos env.yaml y .env en el directorio /app del contenedor.
COPY ./env.yaml /app/env.yaml
COPY .env /app/.env

# Usar conda para crear un entorno con las dependencias especificadas en env.yaml.
RUN conda env create -f env.yaml

# Activar el entorno. 
RUN echo "source activate venv_proyecto" > ~/.bashrc
ENV PATH /opt/conda/envs/venv_proyecto/bin:$PATH

# Copiar todos los archivos en el directorio actual en el host al directorio /app en el contenedor.
COPY . /app

# Definir el comando que se ejecutará cuando se inicie el contenedor.
CMD ["python", "main.py"]