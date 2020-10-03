# En este archivo se almacenan todas las funciones respectivas a la seguridad de la base de datos, como el cifrado de datos.
# Tareas relaccionadas con este archivo en nuestro repositorio de GitHub:
#   #12 Función para encriptar los datos del usuario en la base - 5
#   #13 Función para desencriptar los datos de las bases de datos - 5

import os
from cryptography.fernet import Fernet

# Funcion para escribir y guardar la clave. Se generará un archivo clave.key, es importante guardar este archivo por que es el que vamos a usar tanto para cifrar nuestro mensaje, como para luego descifrarlo de nuevo. Solo se tiene que hacer una vez.
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)


# Funcion para cargar la clave
def cargar_clave():
    return open("clave.key").read()


# Funcion para encriptar dato
def encrypt(data: str, clave):
     data = bytes(data, encoding = "utf-8")
     return Fernet(clave).encrypt(data)

