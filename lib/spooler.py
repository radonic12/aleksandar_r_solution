from lib.api_call import call_api
from lib.constants import url_fetch_specific_pokemon
from lib.pokemon import Pokemon
import json

def spooler(session,pokemon_index:int):
    #Print which pokemon is being processed so it can be used at a starting point in case of an exception
    print('Processing of Pokemon with index',pokemon_index,'started')
    #Initiate pokemon class object
    pokemon_object = Pokemon(pokemon_index=pokemon_index)

    #Fetch and format api url
    url = url_fetch_specific_pokemon.format(counter=pokemon_index)
    #Call api and get status_code and response
    status_code, api_response = call_api(url)
    
    #Break flow on 404 since that means the last pokemon has been processed
    if status_code == 404:
        return pokemon_index, status_code

    #Convert response to json dict
    api_response = json.loads(api_response)

    pokemon_object.populate_object(api_response=api_response)
    
    #Add pokemon to database
    exists = session.query(Pokemon.id).filter_by(id=pokemon_index).first() is not None
    #Update if exists, else insert
    if exists:
        session.merge(pokemon_object)
    else: 
        session.add(pokemon_object)
    session.commit()

    #Increment index so the next pokemon will be fetched
    pokemon_index += 1
    print('Processing of Pokemon with index',pokemon_index,'ended')
    return pokemon_index, status_code