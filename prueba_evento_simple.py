# 1. El Manejador de Eventos (Event Handler)
def cuando_llegue_usuario(nombre_usuario):
    print(f"🎉 EVENTO CAPTURADO: Bienvenido a la plataforma, {nombre_usuario}!")

# 2. El Emisor de Eventos (Event Emitter)
def simular_clic_registro(nombre, funcion_que_escucha):
    print(f"\n[Sistema] El usuario '{nombre}' presionó el botón 'Registrar'.")
    # Disparamos el evento pasando la función como argumento
    funcion_que_escucha(nombre)

# 3. Probamos la reacción
simular_clic_registro("Fernández", cuando_llegue_usuario)