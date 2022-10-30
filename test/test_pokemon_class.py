import unittest
from lib.pokemon import Pokemon

class Test_Pokemon_Class(unittest.TestCase):
    def test_calculate_bmi(self):
        #Make sure the BMI calculator is working correctly
        pokemon_index=0
        pokemon = Pokemon(pokemon_index=pokemon_index)
        test_data = {
            'height':100,
            'weight':200,
            'id': pokemon_index
        }
        bmi = pokemon.calculate_bmi(data=test_data)

        self.assertEqual(bmi,0.02)

    def test_find_game_indices(self):
        #Check that game indices are fetched correctly
        pokemon_index=0
        pokemon = Pokemon(pokemon_index=pokemon_index)
        test_data = {
            "game_indices": [
                {
                    "game_index": 9,
                    "version": {
                        "name": "red",
                        "url": "https://pokeapi.co/api/v2/version/1/"
                    }
                },
                {
                    "game_index": 9,
                    "version": {
                        "name": "blue",
                        "url": "https://pokeapi.co/api/v2/version/2/"
                    }
                },
                {
                    "game_index": 9,
                    "version": {
                        "name": "yellow",
                        "url": "https://pokeapi.co/api/v2/version/3/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "gold",
                        "url": "https://pokeapi.co/api/v2/version/4/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "silver",
                        "url": "https://pokeapi.co/api/v2/version/5/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "crystal",
                        "url": "https://pokeapi.co/api/v2/version/6/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "ruby",
                        "url": "https://pokeapi.co/api/v2/version/7/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "sapphire",
                        "url": "https://pokeapi.co/api/v2/version/8/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "emerald",
                        "url": "https://pokeapi.co/api/v2/version/9/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "firered",
                        "url": "https://pokeapi.co/api/v2/version/10/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "leafgreen",
                        "url": "https://pokeapi.co/api/v2/version/11/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "diamond",
                        "url": "https://pokeapi.co/api/v2/version/12/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "pearl",
                        "url": "https://pokeapi.co/api/v2/version/13/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "platinum",
                        "url": "https://pokeapi.co/api/v2/version/14/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "heartgold",
                        "url": "https://pokeapi.co/api/v2/version/15/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "soulsilver",
                        "url": "https://pokeapi.co/api/v2/version/16/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "black",
                        "url": "https://pokeapi.co/api/v2/version/17/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "white",
                        "url": "https://pokeapi.co/api/v2/version/18/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "black-2",
                        "url": "https://pokeapi.co/api/v2/version/21/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "white-2",
                        "url": "https://pokeapi.co/api/v2/version/22/"
                    }
                }
            ],
        }
        game_indices = pokemon.find_game_indices(data=test_data)

        self.assertEqual(game_indices,'[{"name": "red", "order": 9}, {"name": "blue", "order": 9}, {"name": "leafgreen", "order": 2}, {"name": "white", "order": 2}]')

        #Remove red game, and make sure all other games are still returned
        test_data = {
            "game_indices": [
                {
                    "game_index": 9,
                    "version": {
                        "name": "blue",
                        "url": "https://pokeapi.co/api/v2/version/2/"
                    }
                },
                {
                    "game_index": 9,
                    "version": {
                        "name": "yellow",
                        "url": "https://pokeapi.co/api/v2/version/3/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "gold",
                        "url": "https://pokeapi.co/api/v2/version/4/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "silver",
                        "url": "https://pokeapi.co/api/v2/version/5/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "crystal",
                        "url": "https://pokeapi.co/api/v2/version/6/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "ruby",
                        "url": "https://pokeapi.co/api/v2/version/7/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "sapphire",
                        "url": "https://pokeapi.co/api/v2/version/8/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "emerald",
                        "url": "https://pokeapi.co/api/v2/version/9/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "firered",
                        "url": "https://pokeapi.co/api/v2/version/10/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "leafgreen",
                        "url": "https://pokeapi.co/api/v2/version/11/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "diamond",
                        "url": "https://pokeapi.co/api/v2/version/12/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "pearl",
                        "url": "https://pokeapi.co/api/v2/version/13/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "platinum",
                        "url": "https://pokeapi.co/api/v2/version/14/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "heartgold",
                        "url": "https://pokeapi.co/api/v2/version/15/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "soulsilver",
                        "url": "https://pokeapi.co/api/v2/version/16/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "black",
                        "url": "https://pokeapi.co/api/v2/version/17/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "white",
                        "url": "https://pokeapi.co/api/v2/version/18/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "black-2",
                        "url": "https://pokeapi.co/api/v2/version/21/"
                    }
                },
                {
                    "game_index": 2,
                    "version": {
                        "name": "white-2",
                        "url": "https://pokeapi.co/api/v2/version/22/"
                    }
                }
            ],
        }
        
        pokemon = Pokemon(pokemon_index=pokemon_index)
        game_indices = pokemon.find_game_indices(data=test_data)

        self.assertEqual(game_indices,'[{"name": "blue", "order": 9}, {"name": "leafgreen", "order": 2}, {"name": "white", "order": 2}]')

    def test_find_slot_types(self):
        #Check that game indices are returned correctly
        pokemon_index=0
        pokemon = Pokemon(pokemon_index=pokemon_index)
        test_data = {
            "types": [
                {
                    "slot": 1,
                    "type": {
                        "name": "grass",
                        "url": "https://pokeapi.co/api/v2/type/12/"
                    }
                },
                {
                    "slot": 2,
                    "type": {
                        "name": "poison",
                        "url": "https://pokeapi.co/api/v2/type/4/"
                    }
                }
            ],
        }
        slot_types = pokemon.find_slot(data=test_data)

        self.assertEqual(slot_types, '[{"slot": 1, "name": "grass"}, {"slot": 2, "name": "poison"}]')

        #Remove slot 1
        test_data = {
            "types": [
                {
                    "slot": 2,
                    "type": {
                        "name": "poison",
                        "url": "https://pokeapi.co/api/v2/type/4/"
                    }
                }
            ],
        }
        slot_types = pokemon.find_slot(data=test_data)

        self.assertEqual(slot_types, '[{"slot": 2, "name": "poison"}]')
