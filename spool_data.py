from lib.pokemon import Pokemon
from lib.db import Database
from lib.spooler import spooler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

#Initiate database
engine = create_engine('sqlite:///pokemons.db', echo=True)
db = Database(engine=engine)
#Create table if doesn't exist
db.create_table()
#Initiate session
Session = sessionmaker(bind=engine)
session = Session()

#Initite counter which is used to loop through pokemons
pokemon_index = 1
#Get the pokemon index the spooler last spooled 
max_pokemon_id = session.query(func.max(Pokemon.id)).scalar()
if max_pokemon_id != None:
    pokemon_index = max_pokemon_id+1
    
#Initite status_code which is used to break the while loop
status_code = 200

#Break while loop when index is out of range and no more pokemons to process
while status_code!=404:
    pokemon_index, status_code = spooler(session=session,pokemon_index=pokemon_index)

#Close connections
session.close()
engine.dispose()