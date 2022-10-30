import unittest
from lib.spooler import spooler
from lib.pokemon import Pokemon
from lib.constants import test_db_name
from lib.db import Database
from lib.spooler import spooler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import select
import os
import sqlite3
import pandas as pd

class Test_Spooler(unittest.TestCase):
    def test_spooler(self):
        #Set expected output of test 
        expected_output = [(1, 'Bulbasaur', '64', 69, 7, 1, '[{"name": "red", "order": 153}, {"name": "blue", "order": 153}, {"name": "leafgreen", "order": 1}, {"name": "white", "order": 1}]', '[{"slot": 1, "name": "grass"}, {"slot": 2, "name": "poison"}]', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png')]
        #Delete database if exists
        if os.path.exists(test_db_name):
            os.remove(test_db_name)
        #Initiate database
        engine = create_engine(f'sqlite:///{test_db_name}', echo=True)
        db = Database(engine=engine)
        #Create table if doesn't exist
        db.create_table()
        #Initiate session
        Session = sessionmaker(bind=engine)
        session = Session()
        #Initiate counter which is used to loop through pokemons
        pokemon_index = 1

        #Spool values into test db
        spooler(session=session,pokemon_index=pokemon_index)
        #Close connection and session      
        session.close()
        engine.dispose()

        #Reopen connection and session and make sure inserts are committed
        engine = create_engine(f'sqlite:///{test_db_name}', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        #Select all pokemons from DB
        statement = 'select * from pokemons'
        actual_output = [tuple(list(session.execute(statement))[0])]
        
        #Close connection and session      
        session.close()
        engine.dispose()

        #Make sure actual output equals expected output
        self.assertEqual(expected_output,actual_output)