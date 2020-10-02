# En este archivo se almacenan todas las funciones respectivas a la seguridad de la base de datos, como el cifrado de datos.
# Tareas relaccionadas con este archivo en nuestro repositorio de GitHub:
#   #12 Función para encriptar los datos del usuario en la base - 5
#   #13 Función para desencriptar los datos de las bases de datos - 5



import string
import random

all_characters = string.printable

# La clave puede volver a ser generada con el siguiente codigo
# str_var = list(all_characters)
# random.shuffle(str_var)
# key = ''.join(str_var)
key= """*mh~(B}\)#%lU7 oa4i0IZH_`WdLQ|DsjCzqr8b>k<3pS"X'yuM;,^26-/R!A{g]OJ19F5wvVn:tEPeG=[f@Y?K$cxT&N.+"""

def encrypt(data: str):
    encrypted_message = ""
    for character in data:
        i = all_characters.find(character)
        encrypted_message += key[i]
    return encrypted_message
