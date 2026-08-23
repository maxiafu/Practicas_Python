import re

patron_clave = r"^\w{6,10}$"

#Entrada de Prueba
clave = "prueba"

if re.match(patron_clave, clave):
    print("Formato de clave Valido")
else:
    print("Formato de clace Invalido......")

