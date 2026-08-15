##########..:: 📝 Ejercicio Integrador Avanzado: Sistema de Inventario de Tienda ::..##########

"""Imagina que estás desarrollando el backend para una tienda que vende tanto productos físicos 
como productos digitales."""


# ## Clase Padre Producto
# class Producto():
#     def __init__(self, nombre, precio_base):
#         self.nombre = nombre
#         self.__precio_base = precio_base
        
# # Método obtener_precio_base        
#     def obtener_precio_base(self):
#         return int(self.__precio_base)
        
# # Método obtener_precio_final
#     def obtener_precio_final(self):
#         return self.__precio_base
    
# # Método Obtener_info
#     def obtener_info(self):
#         return f"Producto: {self.nombre} | Precio: {self.obtener_precio_final()}"
    

# ## Clase Hija Producto_fisico
# class ProductoFisico(Producto):
#     def __init__(self, nombre, precio_base, costo_envio):
#         super().__init__(nombre, precio_base)
#         self.costo_envio = costo_envio
        
# # Sobrescribiendo Método Obtener precio final
#     def obtener_precio_final(self):
#         return f"self.obtener_precio_base() + self.costo_envio"
    

# ## Clase Hija Producto_Digital
# class ProductoDigital(Producto):
#     def __init__(self, nombre, precio_base, porcentaje_descuento):
#         super().__init__(nombre, precio_base)
#         self.porcentaje_descuento = porcentaje_descuento
        
# # Sobrescribiendo Método Obtener precio final
#     def obtener_precio_final(self):
#         base = self.obtener_precio_base()
#         descuento = base * (self.porcentaje_descuento / 100)
#         return base - descuento


# # Clase Contenedora Tienda
# class Tienda():
#     def __init__(self, nombre_tienda):
#         self.nombre_tienda = nombre_tienda
#         self.__inventario = []


# #Método Agregar Producto
#     def agregar_producto(self, producto):
#         self.__inventario.append(producto)
        

# #Método Mostrar Inventario
#     def mostrar_inventario(self):
#         print(f"La tienda --->{self.nombre_tienda}<---")
        
#         for producto in self.__inventario:
#             print (f"{producto.obtener_info()}")
            
            
# #Método Calcular Valor de Inventario
#     def calcular_valor_inventario(self):
#         total = 0
#         for producto in self.__inventario:
#             total += producto.obtener_precio_final()
#         return f"El Valor de Inventario = {total}"
    
# p_fisico = ProductoFisico("Silla Gamer", 150, 20)
# p_digital = ProductoDigital("Ebook Python", 50, 10)

# mi_tienda = Tienda("TechStore")

# mi_tienda.agregar_producto(p_fisico)
# mi_tienda.agregar_producto(p_digital)

# mi_tienda.mostrar_inventario()








#############..:: Ejercicio Avanzado: Sistema de Gestión de Alquiler de Vehículos ::..#######################
"""Imagina que estás diseñando el sistema de gestión para una empresa de alquiler de vehículos."""

# ###---> Clase Vehiculo
# class Vehiculo():
#     def __init__(self, marca, modelo, precio_diario):
#         self.marca = marca
#         self.modelo = modelo
#         self.__precio_diario = precio_diario
        
# #Método Obtener_Precio:Diario
#     def obtener_precio_diario(self):
#         return self.__precio_diario
    
    
# #Método Calcular Alquiler
#     def calcular_alquiler(self, dias):
#         return self.obtener_precio_diario() * dias
        
# #Método Obtener_Info
#     def obtener_info(self):
#         return f"{self.marca} {self.modelo} Precio/Día : {self.obtener_precio_diario()}"
    

# ###---> Clase Hija Auto
# class Auto(Vehiculo):
#     def __init__(self, marca, modelo, precio_diario, tiene_gps: bool):
#         super().__init__(marca, modelo, precio_diario)
#         self.tiene_gps = tiene_gps
    
        
# ###---> Sobrescribe calcular_alquiler(self, dias) (Polimorfismo + Condicional):
#     def calcular_alquiler(self, dias):
#         total = self.obtener_precio_diario() * dias
#         if self.tiene_gps:
#             total += (10 * dias)
#         return total
    
    
    
# ###---> Clase Hija Moto
# class Moto (Vehiculo):
#     def __init__(self, marca, modelo, precio_diario, cilindrada: int):
#         super().__init__(marca, modelo, precio_diario)
#         self.cilindrada = cilindrada
        
# ###---> Sobrescribe calcular alquiler
#     def calcular_alquiler(self, dias):
#         total = self.obtener_precio_diario() * dias### Calculando Precio Base
#         if self.cilindrada > 250:
#             total *= 1.20### Aplicando recargo de 20% por día 
#         return total

        

# ####---> Clase Contenedora (EmpresaAlquiler):
# class EmpresaAlquiler():
#     def __init__(self, nombre_empresa):
#         self.nombre_empresa = nombre_empresa
#         self.__flota = []
        
# #Método ---> Agregar Vehiculo
#     def agregar_vehiculo(self, vehiculo):
#         self.__flota.append(vehiculo)
        
# #Método ---> Mostrar Flota
#     def mostrar_flota(self):
#         for vehiculo in self.__flota:
#             print(vehiculo.obtener_info())
            
            
# #---> Método calcular_ingreso_total(self, dias):
#     def calcular_ingreso(self, dias):
#         total = 0
#         for vehiculo in self.__flota:
#             total += vehiculo.calcular_alquiler(dias)
#         return total
    
# #---> Método Buscar por Marcas (Componente de Filtro)
#     def buscar_por_marcas(self, marca_buscada):
#         self.marca_buscada = marca_buscada
#         for vehiculo in self.__flota:
#             if vehiculo.marca.lower() == marca_buscada.lower():
#                 print(vehiculo.obtener_info())
            
# ###########..:: ---> Pruebas <--- ::..###################

# a1 = Auto("Toyota", "Corolla", 50, True)##Creando Auto con GPS
# m1 = Moto("Honda", "CB125", 25, 125)####Creando Moto de baja cilindrada
# m2 = Moto("Yamaha", "MT07", 60, 689)####Creando Moto de alta cilindrada
# empresa = EmpresaAlquiler("MAXAIFU")## Creando Empresa

# ###..:: Agregando los 3 vehiculos a la empresa ::..#####
# empresa.agregar_vehiculo(a1)
# empresa.agregar_vehiculo(m1)
# empresa.agregar_vehiculo(m2)


# #####..:: Mostrando la flota Completa ::..#############
# empresa.mostrar_flota()


# ####..:: Calculando el ingreso Total para alquiler de 3 dias " Toda la FLota "
# ingreso_3_dias = empresa.calcular_ingreso(3)
# print (f"El Ingreso Estimado por 3 días: {ingreso_3_dias} ")

# ###..: Realizando busqueda "Filtrada"
# empresa.buscar_por_marcas("Honda")


#############..:: Ejercicio: Sistema de Gestión de Cuentas Bancarias ::..#######################

"""Imagina que estás construyendo el sistema central de un banco. Habrá cuentas normales, 
cuentas de ahorro y cuentas corrientes, además de una clase contenedora para el banco."""

##Clase Cuenta Bancaria (Padre:)
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo_inicial = saldo_inicial
        
#Método Obtener Saldo
    def obtener_saldo(self):
        return self.__saldo_inicial
    
#Método Depositar
    def depositar(self, monto):
        if monto > 0:
            self.__saldo_inicial += monto
            return True
        return False
            
#Método Retirar
    def retirar(self, monto):
        if monto <= self.obtener_saldo():
            self.__saldo_inicial -= monto
            return True
        return False
            
#Método Obtener Info
    def obtener_info(self):
        return(f"Titular: {self.titular} | Saldo: {self.obtener_saldo()}")
        
        
## Clase Cuenta de Ahorros " Hija"
class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes
        
#Método Aplicar Interes:
    def aplicar_interes(self):
        interes = self.obtener_saldo () * (self.tasa_interes / 100)# Calcula el monto del interés basado en el saldo actual
        self.depositar(interes) #Deposita ese interés en la cuenta
        return float(interes) #Retorna el monto del interés generado (un número float).
        
        
        
##Clase Cuenta Corriente (Hija)
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, porcentaje_comision):
        super().__init__(titular, saldo_inicial)
        self.porcentaje_comision = porcentaje_comision
        
#Sobrescribiendo Método Retirar "Polimorfismo"
    def retirar(self, monto):
        comision = monto * (self.porcentaje_comision / 100) ## Calulando Comisión
        monto_total = monto + comision ##Monto Total (Retiro + la comisión)
        
        return super().retirar(monto_total)# Realizar el retiro del monto_total llamando a la clase padre mediante super().retirar(monto_total)  


##Clase Banco (Clase Contenedora)
class Banco:
    def __init__(self, nombre_banco):
        self.nombre_banco = nombre_banco
        self.__cuentas = []
        
#Método Agregar Cuentas
    def agregar_cuentas(self, cuenta):
        self.__cuentas.append(cuenta)
            
#Método Calcular Total Banco (Foco Acumulador):
    def calcular_total_banco(self):
        total = 0
        for cuenta in self.__cuentas: #cada elemento de la lista es un objeto de tipo CuentaBancaria
            total += cuenta.obtener_saldo()
        return total
        
#Método Filtar Cuentas VIP
    def filtrar_cuentas(self, saldo_minimo):
        for cuenta in self.__cuentas:
            if cuenta.obtener_saldo() >= saldo_minimo:
                print(cuenta.obtener_info())
                
                
                
#####..:: Pruebas de Ejecucuión ::..######
#Crear Cuentas de Ahorro
c1 = CuentaAhorros("Ismael", 1000, 5)#Saldo 1000, 5% de interes
interes_generado = c1.aplicar_interes()
print(f"El Interes Generado para: {c1.titular}, es: --> {interes_generado}")

#Crear Cuenta Corriente
c2 = CuentaCorriente("Yoselin", 500, 2)# Saldo 500, 2% comisión
retiro_exitoso = c2.retirar(100) # Retira $100 + $2 comisión = $102 -> Nuevo saldo: $398
print(f"Retiro {retiro_exitoso} Exitosamente")

#Crear el banco y agregar las cuentas
banco_central = Banco("Banco Central")
banco_central.agregar_cuentas(c1)
banco_central.agregar_cuentas(c2)

#Calcular Saldo Total
total_administrado = banco_central.calcular_total_banco()  # 1050 + 398 = 1448
print(f"\nTotal administrado por el banco: ${total_administrado}")

## Filtrar Cuentas VIP
banco_central.filtrar_cuentas(500)