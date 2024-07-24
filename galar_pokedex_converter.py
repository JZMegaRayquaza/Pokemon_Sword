import math
import json

def calculate_box_row_col(dex):
    '''Given a dex number, output the corresponding box, row, and column the pokemon should be put in.'''
    box = math.ceil(dex / 30)

    dex -= 1
    dex %= 30  # 0 to 29

    row = math.floor(dex / 6) + 1  # 1 to 5
    column = (dex % 6) + 1  # 1 to 6

    return (box, row, column)

def main():
    # Opening JSON file
    with open('galar_pokedex.json') as json_file:
        galar_pokedex = json.load(json_file)

    galar_pokedex_positions = {}
    for pokemon in galar_pokedex:
        position = calculate_box_row_col(galar_pokedex[pokemon])
        galar_pokedex_positions[pokemon] = position

    # Saving to JSON file
    json_file_path = 'galar_pokedex_positions.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(galar_pokedex_positions, json_file, indent=4)
    print(f'Galar Pokédex Positions saved to {json_file_path}')

if __name__ == '__main__':
    main()