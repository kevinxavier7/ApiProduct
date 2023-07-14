from fastapi import APIRouter
from controller.users.apiuser import UserManager
from fastapi import Request
from utils.tools import get_input_data
from utils.tools import try_catch
from middleware.verify_token_route import VerifyTokenRouter

user_router = APIRouter(route_class=VerifyTokenRouter)
user = UserManager()

@user_router.get('/api/users')
@try_catch
async def get_users(request: Request):    
    
    
    data = await get_input_data(request)
    return user.get_user(data)
    
@user_router.post('/api/users')
@try_catch
async def create_user(request: Request):   
    data = await get_input_data(request)
    return user.create_user(data)
        
@user_router.put('/api/users')
@try_catch
async def update_user(request: Request):   
    data = await get_input_data(request)
    return user.update_user(data)       
        
          
    
      
    
      
    
    
    
    


