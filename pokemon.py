import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize()
        height = data['height']
        weight = data['weight']
        types = [type_info['type']['name'] for type_info in data['types']]
        return f"{name} (Height: {height}, Weight: {weight}, Types: {', '.join(types)})"
    else:
        return "Pokémon nicht gefunden."


