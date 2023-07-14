import bcrypt
from database.database import Database
from models.user import User
from sqlalchemy import select
      
    
def encode_password(password):
    
    passwd = str(password).encode('utf-8')
    
    encode_password = bcrypt.hashpw(passwd, bcrypt.gensalt())
    return encode_password

def verify_user_password(data:dict):
    db = Database()
    
    user = db.query(
        select(User.user_id, User.password).where(
            User.username == data['username']
        ))
    
    if user:        
        password = str(data['password']).encode('utf-8')
        if bcrypt.checkpw(password, str(user[0]['password']).encode('utf-8')):
            return True, user[0]['user_id']
        return False, "password invalid"
    return False, "user not found"
    
    
    
    
    