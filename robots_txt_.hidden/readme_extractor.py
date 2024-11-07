import requests
from bs4 import BeautifulSoup
import os

# Función para obtener y recorrer los archivos en una URL
def obtener_contenido(url):
    # Hacer la petición HTTP
    response = requests.get(url)
    
    # Verificar si la respuesta fue exitosa (status 200)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error al acceder a {url}: {response.status_code}")
        return None

# Función para extraer los enlaces de los directorios y archivos
def extraer_enlaces(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []

    # Buscar todos los enlaces en el HTML
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and not href.startswith('..'):  # Filtrar los enlaces de directorios padres
            links.append(href)

    return links

# Función para recorrer recursivamente el directorio
def recorrer_directorios(url):
    # Obtener el contenido de la página
    html = obtener_contenido(url)
    
    if not html:
        return []
    
    # Extraer los enlaces a subdirectorios y archivos
    enlaces = extraer_enlaces(html)
    
    # Lista para almacenar el contenido de los READMEs encontrados
    readmes = []
    
    # Recorrer cada enlace
    for enlace in enlaces:
        # Crear la URL completa
        nueva_url = os.path.join(url, enlace)
        
        # Si el enlace es un directorio, recursivamente obtener el contenido
        if nueva_url.endswith('/'):
            readmes.extend(recorrer_directorios(nueva_url))
        # Si el archivo es un README, obtener su contenido
        elif enlace.lower() == "readme":
            print(f"Encontrado README: {nueva_url}")
            contenido = obtener_contenido(nueva_url)
            readmes.append((nueva_url, contenido))
    
    return readmes

# URL inicial (directorio .hidden)
url_inicial = "http://localhost:6969/.hidden/"

# Llamada para recorrer los directorios
readmes = recorrer_directorios(url_inicial)

# Guardar el contenido de los READMEs en un archivo
if readmes:
    with open("contenidos_readmes.txt", "w", encoding="utf-8") as salida:
        for archivo, contenido in readmes:
            salida.write(f"Archivo: {archivo}\n")
            salida.write(contenido + "\n\n")
else:
    print("No se encontraron archivos README.")
