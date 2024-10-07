import requests
from bs4 import BeautifulSoup

# URL del equipo (puedes cambiarlo según el equipo que desees)
url = "https://www.basketball-reference.com/teams/LAL/2024.html"

# Hacer la solicitud a la página web
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido de la página con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Intentar encontrar el nombre del equipo usando un selector alternativo
    team_header = soup.find('h1')
    if team_header:
        team_name = team_header.get_text().strip()
        print(f"Equipo: {team_name}")
    else:
        print("No se pudo encontrar el nombre del equipo.")
    
    # Buscar el récord de victorias y derrotas en el resumen del equipo
    summary = soup.find('div', {'id': 'meta'})
    if summary:
        # Buscar el texto que contiene el récord (por lo general está en un párrafo)
        paragraphs = summary.find_all('p')
        for paragraph in paragraphs:
            if 'Record:' in paragraph.text:
                record = paragraph.text.split('Record:')[1].split(',')[0].strip()
                print(f"Récord: {record}")
                break
        else:
            print("No se pudo encontrar el récord del equipo.")
    else:
        print("No se pudo encontrar el resumen del equipo.")
else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")