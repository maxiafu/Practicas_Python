# class Estudiante:
#     def __init__(self, nombre, email):
#         self.nombre = nombre
#         self.email = email
        
#     def obtener_info(self):
#         return (f"El estudiante: {self.nombre} | Email: {self.email}")
        
# class Curso:
#     def __init__(self, nombre_curso, cupo_max):
#         self.nombre_curso = nombre_curso
#         self.cupo_max = cupo_max
#         self.__estudiantes = []
        
#     def inscribir_estudiante(self,estudiante):
#         if len(self.__estudiantes) < self.cupo_max:
#             self.__estudiantes.append(estudiante)
#             print(f"El Estudiante: {estudiante.nombre} fue inscrito exitosamente en {self.nombre_curso}")
#         else:
#             print(f"No hay cupos disponibles en {self.nombre_curso} para {estudiante.nombre}")
        
#     def mostrar_inscritos(self):
#         print({self.nombre_curso})
#         for estudiante in self.__estudiantes:
#             print (estudiante.obtener_info())
        
        
# est1 = Estudiante("Ismar Valentina", "ismar@mail.com")
# est2 = Estudiante("Yoselin Villegas", "yoselin@mail.com")

# curso_python = Curso("Python Avanzado", 1)

# curso_python.inscribir_estudiante(est1)
# curso_python.inscribir_estudiante(est2)



# curso_python.mostrar_inscritos()


######..:: Sistema de Carrito de Compras de un E-commerce ::..###########

class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def obtener_detalle(self):
        print (f"El Producto: {self.nombre} | {self.precio}")
        
class carrito():
    def __init__(self, cliente):
        self.cliente = cliente
        self.__productos = []
        
    def agregar_producto(self, producto):
        self.__productos.append(producto)
        print(f"¡{producto.nombre} Agregado al carrito!")
        
    def mostrar_compra (self):
        print (f"----Carrito de {self.cliente}------")
        for producto in self.__productos:
            self.obtener_detalle(producto)
            
            
    def calcular_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.precio
            print (f"Total Acumulado = {total}")
            
            
p1 = Producto("Laptop", 1200)
p2 = Producto("Mouse", 25)

mi_carrito = carrito("Ismael")

mi_carrito.agregar_producto(p1)
mi_carrito.agregar_producto(p2)

mi_carrito.mostrar_compra()

print(f"Total a Pagar {mi_carrito.calcular_total()}")
        
        
    
        