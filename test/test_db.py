import unittest
from lib.pokemon import Pokemon
from lib.db import Database
from lib.constants import test_db_name
from sqlalchemy import create_engine, inspect
import os

class Test_Db(unittest.TestCase):
    def test_create_table(self):
        test_db_path = test_db_name
        #Delete database if exists
        if os.path.exists(test_db_path):
            os.remove(test_db_path)
        #Initiate database
        engine = create_engine(f'sqlite:///{test_db_path}', echo=True)
        db = Database(engine=engine)
        db.create_table()
        #Create table
        insp = inspect(engine)
        table_exists = insp.has_table("pokemons")

        self.assertEqual(True, table_exists)
