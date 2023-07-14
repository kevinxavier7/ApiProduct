from fastapi import APIRouter, Request
from utils.tools import try_catch, get_input_data
from controller.auth.authentication import authentication


login_router = APIRouter()



@login_router.post("/login")
@try_catch
async def login(request:Request):         
    
    data = await get_input_data(request)    
    
    return authentication(data)
    

    