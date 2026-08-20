###..:: Pruebas - Asincronia ::..####
import asyncio


async def preparar_cafe():
    print("Iniciando Café")
    await asyncio.sleep(3)
    print("Café Listo")


async def tostada():
    print("Haciendo Tostadas")
    print("Tostada Lista")


async def main():
    # Ejecuta ambas tareas aprovechando el tiempo de espera
    await asyncio.gather(preparar_cafe(), tostada())


asyncio.run(main())
