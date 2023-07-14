from sqlalchemy import create_engine, insert, update
from sqlalchemy.orm import sessionmaker
from database.connection import db_url
from fastapi.encoders import jsonable_encoder

class Database():
    def __init__(self):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)                      
          
    def get(self, table, arg):
        session = self.Session()
        result = jsonable_encoder(session.query(table).filter(arg).first()) 
        session.close()
        return result
    
    def get_all(self, table):
        session = self.Session()
        result = jsonable_encoder(session.query(table).all())
        session.close()
        return result 
    
    def query(self, sql):
        session = self.Session()
        result = session.execute(sql)
        keys = result.keys()
        return [dict(zip(keys, row)) for row in result]          
    
    def add(self, table, data):
        session = self.Session()        
        result = session.execute(insert(table).values(data))
        session.commit()
        return result.lastrowid
    
    def update(self, table, condicion, data):
        session = self.Session()
        session.execute(update(table).where(condicion).values(data))
        session.commit()
        session.close()
        return True  
    
     
        
       
         
    
    
        