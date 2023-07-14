from database.database import Database
from models.user import User
from fastapi import status
from schemas.uservalidation import CreateUser, UpdateUser
from utils.tools import response, response_error
from .functions import encode_password



class UserManager():
    def __init__(self):
        self.db = Database()        
     
    def get_user(self, data=None):          
        
        if data is None:
            result = self.db.get_all(User)                          
        else:            
            result = self.db.get(User, User.user_id == data['user_id'])  
            if not result:
                return response_error("User not found", status.HTTP_404_NOT_FOUND)        
                 
        return response('list users', result, status.HTTP_200_OK)                    
        
    
    def create_user(self, data:dict):            
        
        request = CreateUser(**data)                  
        
        if request.validate: 
            data['password'] = encode_password(data['password'])      
            self.db.add(User, data)
            data['password']= "****"
            return response(
                "user created successfully",
                data,
                status.HTTP_200_OK
            )
            
       
    def update_user(self, data:dict):
        
        request = UpdateUser(**data)     
        
        if request:
            self.db.update(
                User, User.user_id==data['user_id'], data)
            return response(
                "user updated successfully",
                data,
                status.HTTP_200_OK)
                           
        
        
            
        
        
        
    
