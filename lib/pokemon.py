from lib.constants import slots_of_interest, games_of_interest, class_attributes_types, class_attributes_preprocessing, class_attributes_json_path, special
from lib.db import Base
from sqlalchemy import Column, PickleType, Integer, String
import json

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True)
    name = Column(String)  
    base_experience = Column(String)  
    weight = Column(Integer)
    height = Column(Integer)
    #order = Column(PickleType)
    bmi = Column(Integer)
    game_indices = Column(String)
    slot_types = Column(String)
    front_default_sprite = Column(String)  
    
    def __init__(self,pokemon_index:int) -> None:
        self.pokemon_index = pokemon_index

    def __setattr__(self, name: str, value: any) -> None:
        #Do not do any checks if the attribute is not from the JSON response of the api
        if name not in class_attributes_types.keys():
            self.__dict__[name] = value
            return
        #Check the expected type of attribute
        value_type = class_attributes_types[name]
        #Try converting the type if it not correct and raise error upon error
        if type(value)!= value_type:
            try:
                value = value_type(value)
            except:
                raise TypeError('value',value,' with name',name,'cannot be converted to type', str(value_type), 'for pokemon with index', self.pokemon_index)
        #Check if preprocessing is needed
        if name in class_attributes_preprocessing.keys():
            #Fetch need preprocessing
            preprocessing = class_attributes_preprocessing[name]
            #Apply preprocessing
            value = eval(f'value.{preprocessing}')
        self.__dict__[name] = value

    def calculate_bmi(self, data):
        #Extract needed data
        weight = data['weight']
        height = data['height']
        id = data['id']
        #Double check type
        if not (type(weight) == int or type(weight) == float) or not (type(height) == float or type(height) == int):
            raise ValueError('Height or weight data for pokemon with id', id,'is not formatted as int')

        return weight/(height**2)

    def find_game_indices(self, data):
        game_indices = data['game_indices']
        games = [{'name':d['version']['name'],'order':d['game_index']} for d in game_indices if d['version']['name'] in games_of_interest]
        games = json.dumps(games)
        return games

    def find_slot(self, data):
        types = data['types']
        slot_types = [{'slot':t['slot'],'name':t['type']['name']} for t in types if t['slot'] in slots_of_interest]
        slot_types = json.dumps(slot_types)
        return slot_types  

    def populate_object(self, api_response):
        #Loop through dict of interesting attributes and their json_path in the api_response
        for pokemon_attribute_name, json_path in class_attributes_json_path.items():
            #Some attributes are labelled special if they need to be calculated and cannot be fetched directly
            if json_path != 'special':
                #Split and loop for nested attributes such as front_default_sprite with json_path sprites.front_default
                keys = json_path.split(".")
                json_value = api_response
                for key in keys:
                    json_value = json_value[key]
                pokemon_attribute_value = json_value
            else:
                pokemon_attribute_value = eval(special[pokemon_attribute_name])    
            #Set class attribute and value   
            self.__setattr__(pokemon_attribute_name, pokemon_attribute_value)
        