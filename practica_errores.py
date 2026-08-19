try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Error: NO puedes dividir entre cero")
else:
    print(f" Éxito: El resultado es {resultado}")
finally:
    print(" Fin de la operación.")  # Se ejecuta SIEMPRE (haya error o no)