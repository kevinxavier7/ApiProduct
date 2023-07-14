from ..users.functions import verify_user_password
from .jwt import Auth
from utils.tools import response, response_error
from fastapi import status

def authentication(data:dict):    
    
    user = verify_user_password(data)    
    
    if user[0]:        
        auth = Auth(1)
        token = auth.generate_token(user)
        return response("login succesfull",{
            'user': user[1],
            'token': token,
            'expires': f"{auth.expiration_hours} hour"         
        },status.HTTP_200_OK )
    return response_error(
        user[1], status.HTTP_400_BAD_REQUEST)
    
        
            
        
    
    
    
    