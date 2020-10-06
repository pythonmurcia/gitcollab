# En este archivo se almacenan todas las funciones respectivas a la seguridad de la base de datos, como el cifrado de datos.
# Tareas relaccionadas con este archivo en nuestro repositorio de GitHub:
#   #12 Función para encriptar los datos del usuario en la base - 5
#   #13 Función para desencriptar los datos de las bases de datos - 5

import os
from cryptography.fernet import Fernet

def generate_key():
    """ Funcion para escribir y guardar la clave. Se generará un archivo key.key, es importante guardar este archivo
    por que es el que vamos a usar tanto para cifrar nuestro mensaje, como para luego descifrarlo de nuevo.
    Solo se tiene que hacer una vez.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """ Funcion para cargar la clave
    :return key: Clave para encriptar y desencriptar
    :rtype key: str
    """
    key = open("key.key").read()
    return key


def encrypt(data: str, key):
    """ Funcion para encriptar un dato
    :param data: El dato que vamos a encriptar, como un email o un nombre de usuario
    :type data: str
    :param key: Clave para encriptar y desencriptar
    :type key: str
    :return encrypted_data: El dato encriptado
    :rtype encrypted_data: bytes
    """
    data = bytes(data, encoding = "utf-8")
    encrypted_data = Fernet(key).encrypt(data)
    return encrypted_data


def decrypt(data: bytes, key):
    """ Funcion para desencriptar un dato
    :param data: El dato que vamos a desencriptar
    :type data: bytes
    :param key: Clave para encriptar y desencriptar
    :type key: str
    :return decrypted_data: El dato desencriptado
    :rtype decrypted_data: str
    """
    decrypted_data = Fernet(key).decrypt(data)
    decrypted_data = str(decrypted_data, encoding = "utf-8")
    return decrypted_data