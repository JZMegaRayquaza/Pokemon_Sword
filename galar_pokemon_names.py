import requests
from bs4 import BeautifulSoup
import json

def get_galar_pokedex():
    url = 'https://www.serebii.net/swordshield/galarpokedex.shtml'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    galar_pokedex = {}

    # Find the main table containing the Galar Pokédex entries
    pokedex_tables = soup.find_all('table', {'class': 'tab'})

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for table in pokedex_tables:
        rows = table.find_all('tr')[2:]  # Skip the first two header rows

        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 4:
                galar_dex_number = int(columns[0].get_text(strip=True)[1:])
                pokemon_name = columns[3].get_text(strip=True).lower()
                english_name = ''
                for c in pokemon_name:
                    if c in alphabet:
                        english_name += c
                galar_pokedex[english_name] = galar_dex_number

    return galar_pokedex

def save_pokedex_to_json(pokedex, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(pokedex, json_file, indent=4)

if __name__ == '__main__':
    galar_pokedex = get_galar_pokedex()
    json_file_path = 'galar_pokedex.json'
    save_pokedex_to_json(galar_pokedex, json_file_path)
    print(f"Galar Pokédex saved to {json_file_path}")
