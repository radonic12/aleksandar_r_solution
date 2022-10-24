from lib.api_call import call_api
from lib.constants import class_attributes_json_path, special, url_fetch_specific_pokemon
from lib.classes import Pokemon
import time

#Initite counter which is used to loop through pokemons
pokemon_index = 1
#Initite status_code which is used to break the while loop
status_code = 200
#Tacks number of failed calls
failed_api_calls = 0

#Break while loop when index is out of range and no more pokemons to process
while status_code!=404:
    #Print which pokemon is being processed so it can be used at a starting point in case of an exception
    print('Processing of Pokemon with index',pokemon_index,'started')
    #Initiate pokemon class object
    pokemon_object = Pokemon()

    #Fetch and format api url
    url = url_fetch_specific_pokemon.format(counter=pokemon_index)
    #Call api and get status_code and response
    status_code, api_reponse = call_api(url)
    #Retry api call on failure
    if status_code != 200 and failed_api_calls < 4:
        time.sleep(10)
        failed_api_calls += 1
        continue
    #Reset failed api calls counter
    failed_api_calls = 0

    #Loop through dict of interesting attribues and their json_path in the api_response
    for pokemon_attribue_name, json_path in class_attributes_json_path.items():
        #Some attributes are labelled special if they need to be calclulated and cannot be fetched directly
        if json_path != 'special':
            #Split and loop for nested attributes such as front_default_sprite with json_path sprites.front_default
            keys = json_path.split(".")
            json_value = api_reponse
            for key in keys:
                json_value = json_value[key]
            pokemon_attribue_value = json_value
        else:
            pokemon_attribue_value = eval(special[pokemon_attribue_name])    
        #Set class attribute and value   
        pokemon_object.__setattr__(pokemon_attribue_name, pokemon_attribue_value, pokemon_index)

    #Increment index so the next pokemon will be fetched
    pokemon_index += 1