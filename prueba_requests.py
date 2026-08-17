import requests

# Consultamos la API pública de GitHub
url = "https://api.github.com/users/octocat"
respuesta = requests.get(url)

# Verificamos si la petición fue exitosa (Código 200)
if respuesta.status_code == 200:
    datos = respuesta.json()
    print("--- Datos de la API de GitHub ---")
    print(f"Usuario: {datos['login']}")
    print(f"Nombre: {datos['name']}")
    print(f"Repos públicos: {datos['public_repos']}")
    print(f"Seguidores: {datos['followers']}")
else:
    print(f"Error en la conexión: {respuesta.status_code}")