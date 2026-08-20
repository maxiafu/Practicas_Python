import asyncio
import re


# 1. EVENT HANDLERS (Funciones que reaccionan al evento)
async def validar_email_handler(email: str) -> bool:
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    await asyncio.sleep(0.5)  # Simula tiempo de procesamiento

    if re.match(patron, email):
        print(f"✅ [Validación] El correo '{email}' es válido.")
        return True
    else:
        print(f"❌ [Validación] El correo '{email}' NO tiene formato válido.")
        return False


async def enviar_bienvenida_handler(email: str):
    await asyncio.sleep(1)  # Simula envío por red
    print(f"📧 [Email] Mensaje de bienvenida enviado a '{email}'.")


# 2. EMISOR DEL EVENTO (Captura la acción)
async def procesar_evento_registro(email: str):
    print(f"\n⚡ Evento detectado: 'intento_de_registro' -> {email}")

    # Reaccionamos al evento
    es_valido = await validar_email_handler(email)
    if es_valido:
        await enviar_bienvenida_handler(email)


# 3. BUCLE PRINCIPAL (Simulación de acciones del usuario en tiempo real)
async def main():
    # Simulamos 2 usuarios registrándose casi al mismo tiempo
    await asyncio.gather(
        procesar_evento_registro("desarrollador@empresa.com"),
        procesar_evento_registro("usuario_correo_invalido"),
    )


if __name__ == "__main__":
    asyncio.run(main())
