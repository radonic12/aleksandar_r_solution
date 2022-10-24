games_of_interest = ['red', 'blue', 'leafgreen', 'white']
slots_of_interest = [1,2]

url_fetch_specific_pokemon = 'https://pokeapi.co/api/v2/pokemon/{counter}/'

class_attributes_json_path = {
    'name':'name', 
    'id':'id', 
    'base_experience':'base_experience', 
    'weight':'weight', 
    'height':'height', 
    'order':'order', 
    'bmi':'special', 
    'game_indices':'special', 
    'slot_types':'special', 
    'front_default_sprite':'sprites.front_default'
}

special = {
    'bmi':'pokemon_object.calculate_bmi(api_reponse)',
    'game_indices': 'pokemon_object.find_game_indices(api_reponse)',
    'slot_types': 'pokemon_object.find_slot(api_reponse)'
}

class_attributes_types = {
    'name':str,
    'id':int,
    'base_experience':str,
    'weight':int,
    'height':int,
    'order':dict,
    'bmi':int,
    'game_indices':dict,
    'slot_types':dict,
    'front_default_sprite':str
}

class_attributes_preprocessing = {
    'name': 'title()'
}
