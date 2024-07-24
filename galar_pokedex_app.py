import tkinter as tk
from difflib import get_close_matches
import json
import sys
import os

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Load JSON data
json_path = resource_path('galar_pokedex_positions.json')
with open(json_path) as f:
    pokemon_data = json.load(f)

# Tkinter app setup
root = tk.Tk()
root.title("Pokemon Location Finder")

# Full screen setup
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Function to handle Enter key press
def find_location(event=None):
    pokemon_name = entry.get().strip()
    if pokemon_name in pokemon_data:
        location = pokemon_data[pokemon_name]
        result_text.set(f"Box: {location[0]}, Row: {location[1]}, Column: {location[2]}")
    else:
        closest_matches = get_close_matches(pokemon_name, pokemon_data.keys(), n=5, cutoff=0.6)
        if closest_matches:
            closest_str = ", ".join(closest_matches)
            result_text.set(f"Pokemon not found. Did you mean: {closest_str}?")
        else:
            result_text.set("Pokemon not found.")

    entry.delete(0, tk.END)  # Clear the entry after processing

# GUI Elements
label = tk.Label(root, text="Enter Pokemon Name:")
label.pack(pady=10)

entry = tk.Entry(root, width=50, font=('Arial', 24))  # Increase text box size and change font size
entry.pack(pady=5)

entry.bind('<Return>', find_location)  # Bind Enter key to find_location function

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=('Arial', 18))  # Adjust font size for result display
result_label.pack()

# Run the main loop
root.mainloop()
