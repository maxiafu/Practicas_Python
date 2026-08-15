#####..:: ---> Ejercicio: Sistema de Gestión de Nómina de Empleados  <--- 

# ### Clase Empleado "Padre"
# class Empleado:
#     def __init__(self, nombre, id_empleado, salario_base):
#         self.nombre = nombre
#         self.id_empleado = id_empleado
#         self.__salario_base = salario_base
        
# #Método Obtener Salario_Base
#     def obtener_salario_base(self):
#         return self.__salario_base
    
# #Método Calcular Pago " Devuelve la base numerica : return self.obtener_salario_base"
#     def calcular_pago(self):
#         return self.obtener_salario_base()
    
# #Método Obtener Info
#     def obtener_info(self):
#         return f" ID: {self.id_empleado} |Nombre: {self.nombre} | Pago Final = {self.calcular_pago()}"
        
# ###Clase Empleado tiempo cpmpleto "Hija"
# class EmpleadoTiempoCompleto(Empleado):
#     def __init__(self, nombre, id_empleado, salario_base, bono_presentisimo):
#         super().__init__(nombre, id_empleado, salario_base)
#         self.bono_presentisimo = bono_presentisimo

# #Sobrescribiendo método Cacular Pago
#     def calcular_pago(self):
#         total = 0
#         total = (self.obtener_salario_base() + self.bono_presentisimo)
#         return total
    
    
# #Método Empleado por Comisión
# class EmpleadoPorComision(Empleado):
#     def __init__(self, nombre, id_empleado, salario_base, ventas_realizadas, porcentaje_comision):
#         super().__init__(nombre, id_empleado, salario_base)
#         self.ventas_realizadas = ventas_realizadas
#         self.porcentaje_comision = porcentaje_comision
        
# # Sobrescribiendo Método Calcular_Pago
#     def calcular_pago(self):
#         comision = self.ventas_realizadas *(self.porcentaje_comision / 100)
#         salario_total = (self.obtener_salario_base() + comision)
#         return salario_total
    
# # Clase Contenedora " Empresa"

# class Empresa():
#     def __init__(self, razon_social):
#         self.razon_social = razon_social
#         self.__plantilla = []
        
# #Método Agregar Empleado
#     def agregar_empleado (self, empleado):
#         self.__plantilla.append(empleado)
        
        
# #Método Mostrar Plantilla
#     def mostrar_plantilla(self):
#         print(f"Plantilla de Empresa: {self.razon_social}")
#         for empleado in self.__plantilla:
#             print(empleado.obtener_info())
            
# #Método Calcular_Total_Nomina "Foco Acumulador"
#     def calcular_nomina(self):
#         total_nomina = 0
#         for empleado in self.__plantilla:
#             total_nomina += empleado.calcular_pago()
#         return total_nomina
    
# #Método Filtrar Pagos Mayores " oOnto Minimo"
#     def filtrar_pago(self, monto_minimo):
#         for empleado in self.__plantilla:
#             if empleado.calcular_pago() >= monto_minimo:
#                 print (empleado.obtener_info())
        
        
        
        
# ### Objetos para realizar las pruebas 
# #Empleado a tiempo completo
# e1 = EmpleadoTiempoCompleto("Pedro Pérez", "E001", 1200, 150)

# #Empleado por comision
# e2 = EmpleadoPorComision("Ana Gómez", "E002", 800, 5000, 10)

# #Creo mi empresa
# mi_empresa = Empresa("IAFU Solutions")

# #Agrego "E1 y E2" a mi empresa
# mi_empresa.agregar_empleado(e1)
# mi_empresa.agregar_empleado(e2)

# mi_empresa.mostrar_plantilla()

# total = mi_empresa.calcular_nomina()
# print(f"EL Total a pagar en mi nomina = {total}")

# mi_empresa.filtrar_pago(1320)



#####..:: ---> Ejercicio: Sistema de Inventario de Tienda <--- ::..#####

##Clase Producto"Padre"
class Producto:
    def __init__(self, nombre, codigo, precio_base):
        self.nombre = nombre
        self.codigo = codigo
        self.__precio_base = precio_base
        
#Método Obtener Precio Base "Devuelve el valor numérico de self.__precio_base"      
    def obtener_precio_base(self):
        return self.__precio_base

#Método Calcular Precio final "Devuelve la base numérica (return self.obtener_precio_base())."
    def calcular_precio_final(self):
        return self.obtener_precio_base()
    
#Método Obtener Info
    def obtener_info(self):
        return f"Código: {self.codigo} | Producto: {self.nombre} | Precio Final: {self.calcular_precio_final()}"
    
    
##Clase  Producto Físico "Hija" --> Hereda de la clase Producto
class ProductoFisico(Producto):
    def __init__(self, nombre, codigo, precio_base, costo_envio):
        super().__init__(nombre, codigo, precio_base)
        self.costo_envio = costo_envio

#Sobrescribiendo método Calcular Precio Final
    def calcular_precio_final(self):
        precio_final = 0
        precio_final = (self.obtener_precio_base() + self.costo_envio)
        return precio_final  
    
##Clase Producto Digital " Hija" --> Hereda de la clase Producto
class ProductoDigital(Producto):
    def __init__(self, nombre, codigo, precio_base, porcentaje_descuento):
        super().__init__(nombre, codigo, precio_base)
        self.porcentaje_descuento = porcentaje_descuento


#Sobrescribiendo método Calcular Precio Final
    def calcular_precio_final(self):
        descuento = 0
        precio_final = 0
        descuento = (self.obtener_precio_base() * (self.porcentaje_descuento / 100))
        precio_final = (self.obtener_precio_base() - descuento)
        return precio_final
    
    

##Clase Tienda "Clase Contenedora"
class Tienda:
    def __init__(self, nombre_tienda):
        self.__inventario = []
        
#Método Agregar Producro a Lista Privada"inventario"
    def agregar_producto(self, producto):
        self.__inventario.append(producto)
        
#Método mostar inventario
    def mostrar_inventario(self):
        for producto in self.__inventario:
            print (producto.obtener_info())
            
#Método Calcular el valor total del inventario
    def valor_total_inv(self):
        total = 0
        for producto in self.__inventario:
            total += producto.calcular_precio_final()
        return total
    
#Método Filtrar_Productos
    def filtrar_productos(self, precio_minimo):
        for producto in self.__inventario:
            if producto.calcular_precio_final() >= precio_minimo:
                print (producto.obtener_info())
                
                
###..::--> objetos para Pruebas <--::..####
# Crear Producto fisico
p1 = ProductoFisico("Teclado Mecánico", "P001", 80, 10)
#Crear Producto Digital
p2 = ProductoDigital("Curso Python", "P002", 50, 20)
# Crear la tienda
mi_tienda = Tienda("IAFU_STORE")

#Agragando los productos creados a la nueva tienda
mi_tienda.agregar_producto(p1)
mi_tienda.agregar_producto(p2)

#Mostrando el Inventario
mi_tienda.mostrar_inventario()

#Calcula e imprime directamente en consola el total del inventario:
print (f"\nValor total de Inventario: $ {mi_tienda.valor_total_inv()}")

#Muestra los productos con precio mayor o igual a $50
mi_tienda.filtrar_productos(50)
