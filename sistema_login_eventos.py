import asyncio
import re

# 1. MANEJADOR DE EVENTO (Handler asincrónico + Regex)
async def procesar_evento_login(usuario: str, clave: str):
    patron_clave = r"^\w{6,10}$"
    
    print(f"⚡ Evento recibido: Intento de inicio de sesión de '{usuario}'...")
    await asyncio.sleep(1)  # Simula tiempo de respuesta del servidor
    
    if re.match(patron_clave, clave):
        print(f"✅ [ÉXITO] Clave de '{usuario}' válida. Acceso concedido.\n")
    else:
        print(f"❌ [ERROR] Clave de '{usuario}' inválida. Debe tener de 6 a 10 caracteres.\n")

# 2. BUCLE PRINCIPAL (Simula varios eventos ocurriendo casi al mismo tiempo)
async def main():
    await asyncio.gather(
        procesar_evento_login("admin", "clave123"),   # Válida (8 caract)
        procesar_evento_login("guest", "123")         # Inválida (3 caract)
    )

if __name__ == "__main__":
    asyncio.run(main())