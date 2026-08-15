# 1. Crea una Clase Padre llamada 'Producto':
#    - En su constructor (__init__), recibe 'nombre' y 'precio'.
#    - Crea un método 'obtener_info()' que devuelva: 
#      "Producto: [nombre] | Precio: $[precio]"

# 2. Crea una Clase Hija llamada 'Libro' que herede de 'Producto':
#    - En su constructor, recibe 'nombre', 'precio' y 'autor'.
#    - Crea un método propio llamado 'mostrar_autor()' que devuelva:
#      "Autor del libro: [autor]"

# class Producto:
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio
    
# class libro(Producto):
#     def mostrar_autor(self):
        
        
        
#####..:: Ejemplo para Programación Orientada a Objeto ::..######

#####..:: Clase Padre (Producto) ::..######

# class Producto():
#     def __init__(self, nombre , precio):
#         self.nombre = nombre
#         self.precio = precio
# ####..:: Creando Metodo Obtener_Info ::..#####
#     def obtener_info (self):
#         return f"Nombre: {self.nombre} | Precio: {self.precio}"
    
    
# ####..:: Creando Clase Hija ::..######
# class Libro(Producto):
#     def __init__(self, nombre, precio, autor):
#         super().__init__(nombre, precio) ####para inicializar la parte del padre.
#         self.autor = autor ##Asigna el autor a su propio atributo (self.autor = autor).
    
# ####..:: Creando Metodo Propio de clase Hija ::..#####
#     def mostrar_autor(self):
#         return f"Autor del Libro: {self.autor}"

# ####..:: Creando Objeto ::..#######    
# mi_libro = Libro("Cien Años de Soledad", 25, "Gabriel García Márquez")


# ####..:: Imprimiendo Métodos ::..#######
# print(mi_libro.obtener_info())
# print(mi_libro.mostrar_autor())



####..:: Ejercicio 2 POO ::..#######
# class Empleado():
#     def __init__(self, nombre, salario_base):
#       self.nombre = nombre
#       self.salario_base = salario_base
      
#     def calcular_salario(self):
#           return f"Salario Base de un Empleado es = {self.salario_base}"
      

# class Gerente(Empleado):
#     def __init__(self, nombre, salario_base, bono):
#         super().__init__(nombre, salario_base)
#         self.bono = bono
        
#     def calcular_salario(self):
#         return f"El Salario base de un Gerente es  = {self.salario_base} y la Bonificación es = {self.bono}, para un total = {self.salario_base + self.bono}"
        
          
          
# emp = Empleado("Carlos", 1000)
# ger = Gerente("Ana", 2000, 500)

# # print(emp.calcular_salario())
# # print (ger.calcular_salario())



# #######..:: Ejercicio de POO N# 3 ::..###########

# class CuentaBancaria():
#     def __init__(self, titular, saldo_inicial):
#         self.titular = titular
#         self.__saldo = saldo_inicial  ##define atributo saldo como privado

#     def depositar(self, monto):
#         self.__saldo += monto
        
    
#     def obtener_saldo(self):
#         return self.__saldo
    
# class CuentaAhorros(CuentaBancaria):
#     def __init__(self, titular, saldo_inicial, tasa_interes ):
#         super().__init__(titular, saldo_inicial)###Hereda de clase Padre "CuentaBancaria"
#         self.tasa_interes = tasa_interes### Atributo porpio de clase hija "CuentaAhorros"
        
#     def aplicar_interes(self):
#         interes = self.obtener_saldo() * self.tasa_interes
#         self.depositar(interes)
#         return f"Se Aplico el interes {interes}. Nuevo Saldo {self.obtener_saldo()}"

# mi_cuenta = CuentaAhorros("Ismar", 1000, 0.05)
# print(f"El Saldo inicial es: {mi_cuenta.obtener_saldo()}")
# print(f"{mi_cuenta.aplicar_interes()}")



# #####..:: Ejercicio POO ::..############

# #####..:: Creando Clase Padre "Parte #1" ::..######
# class Vehiculo():
#     def __init__(self, marca, modelo, nivel_combutible):
#         self.marca = marca
#         self.modelo = modelo
#         self.__nivel_combustible = nivel_combutible ###Variable Privada
        
# #..:: Creando Método obtener_combustible::..#
#     def obtener_combustible(self):
#         return f"El nivel de combustible Actual es = {self.__nivel_combustible}"
    
# #..:: Creando Método recargar_combustible::..#
#     def recargar_combustible(self, cantidad):
#         self.__nivel_combustible += cantidad
        
# #..:: Creando Método Desplazarse::..#
#     def desplazarse(self):
#         return f"El Vehículo está avanzando"
    
# #####..:: Creando Clase Hija "Parte #2" ::..######
# class Auto(Vehiculo):
#     def __init__(self, marca, modelo, nivel_combutible, num_puertas):
#         super().__init__(marca, modelo, nivel_combutible)
#         self.num_puertas = num_puertas
        
# #..:: Sobrescribe el método desplazarse() (Polimorfismo) ::..#
#     def desplazarse(self):
#         return f"El Auto: {self.marca} {self.modelo} Conduce por la carretera"
        
        
        
# #####..:: Creando Clase Hija "Parte #3" ::..######
# class Camion(Vehiculo):
#     def __init__(self, marca, modelo, nivel_combutible, capacidad_carga_ton):
#         super().__init__(marca, modelo, nivel_combutible)
#         self.capacidad_carga_ton = capacidad_carga_ton
        
# #..:: Sobrescribe el método desplazarse() (Polimorfismo) ::..#
#     def desplazarse (self):
#         return f"El Camión {self.marca}, {self.modelo} Trasporta carga pesada"
    

# # --- CREACIÓN DE OBJETOS Y BUCLE ---
    
# mi_auto = Auto ("Toyota", "Corolla", 50, 4)
# mi_camion = Camion ("Volvo", "FH16", 120, 20)
# flota = [mi_auto, mi_camion]


# for vehiculo in flota:
#     print(vehiculo.desplazarse())
        


#######..:: Ejercicio POO : Sistema de Gestión de Clinica ::..#######
# class PersonalMedico():
#     def __init__(self, nombre, id_empleado, salario_base):
#         self.nombre = nombre
#         self.id_empleado = id_empleado
#         self.__salario_base = salario_base
        
#     def obtener_salario(self):
#         return self.__salario_base
    
#     def realizar_turno(self):
#         return f"El Personal Médico esta disponible para la atención"
    
    
# class Doctor(PersonalMedico):
#     def __init__(self, nombre, id_empleado, salario_base, especialidad):
#         super().__init__(nombre, id_empleado, salario_base)
#         self.especialidad = especialidad
        
#     def realizar_turno(self):
#         return f"El Doctor {self.nombre}, {self.especialidad} está atendiendo consultas médicas"
    
    
# class Cirujano(PersonalMedico):
#     def __init__(self, nombre, id_empleado, salario_base, num_operaciones):
#         super().__init__(nombre, id_empleado, salario_base)
#         self.num_operaciones = num_operaciones
        
#     def realizar_turno(self):
#         return f"El Cirujano {self.nombre}, está realizando una operación en Quirófano"
    
# doc = Doctor("Ismael Fernández", "DOC-005", 1985, "Cardiología")
# cir = Cirujano("Ismar Valentina", "CIR-2010", 4500, 12)
# equipo = [doc, cir]

# for Turnos in equipo:
#     print (Turnos.realizar_turno())

# nomina_total = 0
# for persona in equipo:
#     nomina_total += persona.obtener_salario()
# print(f"La Nomina Total a Pagar es: ${nomina_total}")


#######..:: Ejercicio POO : Videojuego "Batalla de personajes" ::..#######

# class Personaje:
#     def __init__(self, nombre, puntos_vida):
#         self.nombre = nombre
#         self.__puntos_vida = puntos_vida
        
#     def obtener_vida(self):
#         return self.__puntos_vida
    
#     def recibir_dano (self, cantidad):
#         self.__puntos_vida -= cantidad
#         if self.__puntos_vida < 0:
#             self.__puntos_vida = 0
#             print (f"La vida es {self.__puntos_vida}, no puede ser negativa")
            
#     def esta_vivo(self):
#         if self.__puntos_vida > 0:
#             return True
#         elif self.__puntos_vida == 0:
#             return False
                
#     def atacar(self, objetivo):
#         return f"El Personaje Ataca"
    
    
# class Guerrero(Personaje):
#     def __init__(self, nombre, puntos_vida, fuerza):
#         super().__init__(nombre, puntos_vida)
#         self.fuerza = fuerza
        
#     def atacar(self, objetivo):
#         print (f"{self.nombre} ataca con su espada causando {self.fuerza} de daño")
    
#         objetivo.recibir_dano(self.fuerza)
        
# class Mago(Personaje):
#     def __init__(self, nombre, puntos_vida, poder_magico):
#         super().__init__(nombre, puntos_vida)
#         self.poder_magico = poder_magico
        
#     def atacar(self, objetivo):
#         print(f"{self.nombre} lanza un hechizo causando {self.poder_magico} de daño")
        
#         objetivo.recibir_dano(self.poder_magico)
        
# guerrero = Guerrero("Thor", 100, 30)
# mago = Mago("Gandalf", 80, 40)
# guerrero.atacar(mago)
# print(f"Vidas Restantes del Mago = {mago.obtener_vida()}")

# mago.atacar(guerrero)
# print(f"Vidas Restantes del Guerrero = {guerrero.obtener_vida()}")





#######..:: Ejercicio POO : Ejercicio: Sistema de Cursos Online" ::..#######

# class Estudiante:
#     def __init__(self, nombre, email):
#         self.nombre = nombre
#         self.email = email
        
#     def obtener_info(self):
#         return f"Estudiante {self.nombre} | Email: {self.email}"
    
    
# class Curso:
#     def __init__(self, nombre_curso, cupo_max):
#         self.nombre_curso = nombre_curso
#         self.cupo_max = cupo_max
        
#         self.__estudiantes = []
        
#     def inscribir_estudiante(self, estudiante):
#         if len(self.__estudiantes) < self.cupo_max:
#             self.__estudiantes.append(estudiante)
#             print(f"El estudiante: {estudiante} fue inscrito en el Curso: {self.nombre_curso}")
#         else:
#             print(f"No hay cupos disponibles en: {self.nombre_curso} para Estudiante : {estudiante}")
            
#     def mostrar_inscritos(self):
#         print(f"{self.nombre_curso}")   

#         for estudiante in self.__estudiantes:
#             print (estudiante.self.obtener_info())
            
# est1 = Estudiante("Carlos Pérez", "carlos@mail.com")
# est2 = Estudiante("María Gómez", "maria@mail.com")

# curso_python = Curso("Python Avanzado", 1)


# curso_python.inscribir_estudiante(1)
    
        


######..:: Ejercicio POO: Carrito de compras deun E-commerce ::..#######

#Creando Clase Producto:
# class Producto:
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio
        
#     def obtener_detalle(self): ####Metodo
#         return f"Producto: {self.nombre} | Precio: {self.precio}"
    
# class Carrito():
#     def __init__(self, cliente):
#         self.cliente = cliente
#         self.__productos = []  ####Lista Privada "Encapsulada"
        
#     def agregar_producto(self, producto):
#         self.__productos.append(producto)###Agregando el parametro "producto del metodo agregar_producto" a la lista privada "self.__productos"
#         print(f"¡ El Producto: {producto.nombre} fue agregado al Carrito !")
        
        
#     def mostrar_compra(self):
#         print(f"---> Carrito {self.cliente} <---")##Imprime el Cliente
#         for producto in self.__productos:
#             print(producto.obtener_detalle())
#             #self.obtener_detalle(producto)####Recorro la lista privada y llamo al método "obtener_detalle" de cada producto
            
#     def calcular_total(self):
#         total = 0
#         for producto in self.__productos:
#             total += producto.precio
#         return f"{total}"
            
            
# ######Pruebas: Paso a Paso
# #Creando dos productos Individuales
# p1 = Producto("Laptop", 1200)
# p2 = Producto ("Mouse", 25)

# #Creando carrito para un cliente
# mi_carrito = Carrito("Ana")

# #Agregando los objetos de "p1 y p2" al objeto "mi_carrito"
# mi_carrito.agregar_producto(p1)
# mi_carrito.agregar_producto(p2)

# #Mostar el contenido y el total
# mi_carrito.mostrar_compra()

# total_pagar = mi_carrito.calcular_total()
# print (f"Total a Pagar: $ {total_pagar}")



#####..:: Ejercicio POO: Sistema de Biblioteca y Libros ::..######

###Clase Libro
class Libro:
    def __init__(self, titulo, autor, num_pag):
        self.titulo = titulo
        self.autor = autor
        self.num_pag = num_pag
        
### Método Obtener_info
    def obtener_info(self):
        return f"{self.titulo} por {self.autor} {self.num_pag} págn."
    
####Clase Biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__catalogos = []

####Método agregar Libro
    def agregar_libro(self, libro):
        self.__catalogos.append(libro)
        print(f"¡Libro '{libro.titulo}' añadido a la biblioteca {self.nombre}")
        
####Método Mostrar Catalogo
    def mostar_catalogo(self):
        print(f"---> Catálogo de: {self.nombre} <---")
        for libro in self.__catalogos:
            print (f"{libro.obtener_info()}")
            
####Método Calcular el total de las páginas
    def calcular_total_paginas(self):
        total_paginas = 0
        for libro in self.__catalogos:
            total_paginas += libro.num_pag
        return total_paginas

####Creando dos libros independientes
l1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 471)
l2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)

####Crenado una biblioteca
mi_biblio = Biblioteca("Biblioteca Central")


###Agrega ambos libros a la biblioteca
mi_biblio.agregar_libro(l1)
mi_biblio.agregar_libro(l2)


####LLamando a mi_blioteca mostrar catalogo
mi_biblio.mostar_catalogo()

####Calculo e imprimo las paginas acumuladas
total_pag_acumulada = mi_biblio.calcular_total_paginas()
print(f"Total de las Páginas en Cátalogo_ {mi_biblio.calcular_total_paginas()}")
print("Otro procedimiento, mismo resultado")
print(f"Total de Páginas: {total_pag_acumulada}")

