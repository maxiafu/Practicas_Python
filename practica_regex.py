import re

patron_clave = r"^\w{6,10}$"

#Entrada de Prueba
clave = "prueba"

if re.match(patron_clave, clave):
    print("Formato de clave Invalida")
else:
    print("Formato Valido......")

