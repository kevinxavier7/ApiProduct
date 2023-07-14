from sqlalchemy import Integer, String, Column, func, DateTime
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key= True, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False) 
    full_name = Column(String(100), nullable=False)   
    created_at = Column(DateTime, default = func.current_timestamp())
    updated_at = Column(DateTime, onupdate= func.current_timestamp())
    
    
    