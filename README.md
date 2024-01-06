# Deploy-Docker

# Generador de datos y notificador por correo

Este proyecto es una aplicación de Python diseñada para generar datos aleatorios de usuarios, incluyendo identificaciones, país de residencia, límite de crédito, y más. Posteriormente, realiza consultas SQL en estos datos y envía los resultados seleccionados por correo electrónico.

## Características

- Generación de datos aleatorios de usuarios con Faker.
- Consultas SQL utilizando SQLite.
- Envío automático de resultados por correo electrónico.

## Tecnologías Utilizadas

- Python
- Pandas
- SQLite
- Faker
- SMTPLib

## Instalación

Primero, clona el repositorio:

```bash
git clone [URL del Repositorio]
cd [Nombre del Repositorio]
```

Construye y ejecuta la imagen Docker:
```bash
docker build -t nombre_de_tu_imagen .
docker run nombre_de_tu_imagen
```

## Configuración
- Archivo .env: Crea un archivo .env en la raíz del proyecto con las siguientes variables:

```bash
SENDER_EMAIL=TuCorreo@gmail.com
RECEIVER_EMAIL=Destinatario@gmail.com
PASSWORD=TuContraseña
```

- Archivo env.yaml: Este archivo contiene las dependencias necesarias para el entorno Conda, ya está configurado y listo para usar.

## Uso
La aplicación se ejecuta automáticamente al iniciar el contenedor Docker. Realiza las siguientes acciones:

Genera un conjunto de datos de 3000 usuarios con información aleatoria.
Realiza una consulta SQL para filtrar datos específicos.
Envía el resultado de la consulta por correo electrónico.
