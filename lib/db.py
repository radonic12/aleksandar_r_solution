from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database():    
    def __init__(self,engine) -> None:
        self.engine = engine

    def create_table(self):
        Base.metadata.create_all(self.engine)
        