from lib.constants import slots_of_interest, games_of_interest, class_attributes_types, class_attributes_preprocessing

class Pokemon():
    def __setattr__(self, name: str, value: any, pokemon_index:int) -> None:
        #Check the expected type of attribute
        value_type = class_attributes_types[name]
        #Try converting the type if it not correct and raise error upon error
        if type(value)!= value_type:
            try:
                value = value_type(value)
            except:
                raise TypeError('value',value,'cannot be converted to type', str(value_type), 'for pokemon with index', pokemon_index)
        #Check if preprocessing is needed
        if name in class_attributes_preprocessing.keys():
            #Fetch need preprocessing
            preprocessing = class_attributes_preprocessing[name]
            #Apply preprocessing
            value = eval(f'value.{preprocessing}')
        self.__dict__[name] = value

    def calculate_bmi(self, data):
        weight = data['weight']
        height = data['height']
        id = data['id']

        if not (type(weight) == int or type(weight) == float) or not (type(height) == float or type(height) == int):
            raise ValueError('Height or weight data for pokemon with id', id,'is not formatted as int')

        return weight/height

    def find_game_indices(self, data):
        game_indices = data['game_indices']
        games = [{'name':d['version']['name'],'order':d['game_index']} for d in game_indices if d['version']['name'] in games_of_interest]

        return games

    def find_slot(self, data):
        types = data['types']
        slot_types = [{'slot':t['slot'],'name':t['type']['name']} for t in types if t['slot'] in slots_of_interest]
        
        return slot_types  
