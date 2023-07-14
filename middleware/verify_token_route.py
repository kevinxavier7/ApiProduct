from fastapi import Request, status
from fastapi.routing import APIRoute
from controller.auth.jwt import Auth
from utils.tools import response_error, try_catch



class VerifyTokenRouter(APIRoute):    
    def get_route_handler(self):
        route_main = super().get_route_handler()
        
        @try_catch
        async def verify_token_middleware(request:Request):
            auth = Auth(1)
            token = request.headers['Authorization'].replace("Bearer ","")                  
            verify_token = auth.verify_token(token)         
            if verify_token[0]:
                return await route_main(request)
            return response_error(verify_token[1], status.HTTP_400_BAD_REQUEST)
        return verify_token_middleware