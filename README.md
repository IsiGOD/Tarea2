Iniciar los Contenedores

Construir las Imágenes y Levantar los Contenedores:
docker-compose up --build
Este comando utiliza el archivo docker-compose.yml para construir las imágenes definidas en los Dockerfiles y luego inicia los contenedores.

Ver los Logs de los Contenedores:
docker-compose logs
Este comando muestra los logs combinados de todos los contenedores especificados en el archivo docker-compose.yml.

Ver los Logs de un Contenedor Específico (por ejemplo, mi-app):
docker-compose logs mi-app
Muestra los logs específicos del contenedor mi-app.

Ejecutar un Comando en un Contenedor en Ejecución (por ejemplo, ejecutar un script de Python en el contenedor mi-app):
docker exec -it mi-app python app.py
Este comando permite ejecutar comandos dentro de un contenedor en ejecución. En este caso, se ejecuta el script Python app.py dentro del contenedor mi-app.

Detener y Eliminar los Contenedores:
docker-compose down
Detiene y elimina los contenedores definidos en el archivo docker-compose.yml. También elimina las redes y volúmenes asociados.

DOCKERFILE:
FROM python:3.8-slim: Indica que la imagen base para este contenedor será python:3.8-slim. La imagen python:3.8-slim es una versión ligera (slim) de Python 3.8, que contiene lo esencial para ejecutar aplicaciones Python.

WORKDIR /app: Establece el directorio de trabajo dentro del contenedor en /app. Este será el directorio predeterminado para ejecutar comandos y también para copiar archivos.

COPY requirements.txt .: Copia el archivo requirements.txt del directorio local (fuera del contenedor) al directorio /app dentro del contenedor. Este archivo suele contener las dependencias de Python necesarias para la aplicación.

RUN pip install --no-cache-dir -r requirements.txt: Ejecuta el comando pip install dentro del contenedor para instalar las dependencias definidas en requirements.txt. La opción --no-cache-dir evita el almacenamiento en caché de los archivos descargados durante la instalación.

COPY . .: Copia todos los archivos y directorios desde el directorio local al directorio /app dentro del contenedor. Esto incluirá todos los archivos de la aplicación, como scripts, código fuente, y cualquier otro archivo necesario para ejecutar la aplicación.

DOCKER-COMPOSE

version: '3': Indica la versión de la especificación de Docker Compose que se va a utilizar. En este caso, se utiliza la versión 3.

services:: Aquí se definen los servicios que forman parte de la aplicación.

a. mongo:: Este es el servicio que utilizará una imagen de MongoDB.

image: mongo:latest: Indica que se utilizará la última versión de la imagen oficial de MongoDB disponible en Docker Hub.

container_name: mi-mongo: Asigna el nombre "mi-mongo" al contenedor que se creará a partir de este servicio.

ports:: Mapea el puerto 27017 del host al puerto 27017 del contenedor, permitiendo la comunicación con la instancia de MongoDB.

volumes:: Monta un volumen llamado ./mongo-data en /data/db dentro del contenedor. Esto se utiliza para persistir los datos de MongoDB fuera del contenedor, de modo que los datos no se pierdan cuando el contenedor se detenga o se elimine.

b. mi-app:: Este servicio se construirá a partir de un Dockerfile local y se conectará al servicio de MongoDB.

build:: Se especifica cómo construir la imagen del contenedor. En este caso, se utiliza el contexto actual (., el directorio donde se encuentra el docker-compose.yml) y el Dockerfile llamado Dockerfile en ese contexto.

container_name: mi-app: Asigna el nombre "mi-app" al contenedor que se creará a partir de este servicio.

depends_on:: Especifica que este servicio depende del servicio mongo, lo que significa que el servicio mi-app se iniciará después de que el servicio mongo esté completamente operativo.

ports:: Mapea el puerto 5000 del host al puerto 5000 del contenedor, permitiendo la comunicación con la aplicación que se ejecuta dentro del contenedor.
