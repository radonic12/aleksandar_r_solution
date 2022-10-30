games_of_interest = ['red', 'blue', 'leafgreen', 'white']
slots_of_interest = [1,2]

url_fetch_specific_pokemon = 'https://pokeapi.co/api/v2/pokemon/{counter}/'

class_attributes_json_path = {
    'name':'name', 
    'id':'id', 
    'base_experience':'base_experience', 
    'weight':'weight', 
    'height':'height', 
    'bmi':'special', 
    'game_indices':'special', 
    'slot_types':'special', 
    'front_default_sprite':'sprites.front_default'
}

special = {
    'bmi':'self.calculate_bmi(api_response)',
    'game_indices': 'self.find_game_indices(api_response)',
    'slot_types': 'self.find_slot(api_response)'
}

class_attributes_types = {
    'name':str,
    'id':int,
    'base_experience':str,
    'weight':int,
    'height':int,
    'bmi':int,
    'game_indices':str,
    'slot_types':str,
    'front_default_sprite':str
}

class_attributes_preprocessing = {
    'name': 'title()'
}

test_db_name = 'test.db'
