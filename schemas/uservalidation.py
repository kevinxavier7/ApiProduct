from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class CreateUser(BaseModel):    
    username:str = Field(required=True)
    password:str = Field(required=True)
    email : EmailStr =  Field(required=True)
    full_name : str = Field(required=True)

class UpdateUser(BaseModel):
    user_id:int = Field(required=True)
    email : Optional[EmailStr]
    full_name : Optional[str] 
    