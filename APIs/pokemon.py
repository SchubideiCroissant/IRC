import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize()
        types = [type_info['type']['name'].capitalize() for type_info in data['types']]
        height = data['height']
        weight = data['weight']
        return f"{name} (Types: [{', '.join(types)}], Height: {height}, Weight: {weight})"
    else:
        return "Pokémon nicht gefunden."


