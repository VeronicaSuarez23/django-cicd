# Notas de despliegue simulado

## Requisitos
- Git
- Docker y Docker Compose

## Pasos
1. Clonar el repositorio:
   git clone https://github.com/VeronicaSuarez23/django-cicd.git
2. Entrar a la carpeta:
   cd django-cicd
3. Levantar los servicios:
   docker compose up --build
4. Abrir el navegador en http://localhost:8000
5. Detener los servicios:
   docker compose down

## Validación
- La página principal muestra "Hola desde Django con CI/CD".
- docker ps muestra los contenedores web y db activos.

## Pipeline
- Job test: instala dependencias y ejecuta pruebas con PostgreSQL.
- Job docker-build: construye la imagen y la guarda como artefacto.
- La publicación en DockerHub es simulada.