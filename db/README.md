## /db/
En el directorio `db/` se encuentran todos los archivos relaccionados con las bases de datos en GitCollab, todas las **funciones de conexion, seguridad o uso de bases de datos** A continuación se explican por tablas el contenido de cada uno de los archivos de este directorio, junto con sus tareas correspondientes.

### __init__.py
El archivo `__init.py` es un archivo creado para que el interprete catalogue este directorio como un paquete de Python.

### security.py
En el archivo `security.py` se encuentran todas las funciones que tienen relacción con la seguridad de las bases de datos de GitCollab.
| Archivo | Tareas relaccionadas | Descripción |
|---------|----------------------|-------------|
| `security.py` | #12, #13	 | En este archivo se encuentran todas las funciones relaccionadas con la seguridad de nuestras bases de datos |
El contenido del archivo es el siguiente:
| Nombre | Tipo | Tareas relaccionadas | Descripción | Estado |
| `encrypt()` | función | #12 | `encrypt` es utilizada para encriptar datos en las bases de datos | Por hacer |
| `decrypt()` | función | #13 | `decrypt` es utilizada para desencriptar datos en las bases de datos | Por hacer |
