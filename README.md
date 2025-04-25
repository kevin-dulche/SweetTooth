# SweetTooth

## Proyecto: Gestión De Consultorio Dental

### Instalación y ejecución:

**Requisitos:**

* Tener instalado Docker.
    * Si no lo tienes instalado ir a [Docker](https://www.docker.com/).

1. Hacer el git clone al proyecto

2. Entrar a la carpeta del proyecto y al mismo nivel de donde esta la carpeta `app` ejecutar el siguiente comando: `docker-compose up -d --build`


3. Para confirmar que se levantaron los contenedores y que estan en ejecución, ejecutar: `docker ps`

3. Para ver la ejecucion del programa abrir en su navegador: `http://localhost:8000/`

### Detener la ejecución de los contenedores

Para terminar la ejecución del programa, ejecutar el siguiente comando: `docker-compose stop`

Ejecutar nuevamente `docker ps` para asegurarse que ya termino la ejecución de ambos contenedores.

Cuando quieras volver a levantar los contenedores usar: `docker-compose start`

### Nota: Cada que modifiques algo y lo quieras probar debes hacer `docker-compose up -d --build`

#### Por el momento se encuentra en modo de pruebas