from fastapi.responses import JSONResponse
from fastapi import status, Request


def try_catch(func):
    
    async def wrapper(request: Request):
        
        try:                      
            return await func(request)
               
        except Exception as e:
           return JSONResponse({
               'error': str(e)
           }, status.HTTP_400_BAD_REQUEST)        
            
    return wrapper

def response( message, data, statuscode):
    return JSONResponse({
        'message': message,
        'data': data
    }, statuscode)
    
def response_error( message,statuscode):
    return JSONResponse({
        'error': message,        
    }, statuscode)
    
async def get_input_data(request:Request):
    if request.method == 'GET':
        data = dict(request.query_params)
        data = None if data =={} else data
        return data
    else:             
        data = await request.json()        
        return data