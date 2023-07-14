from fastapi import APIRouter, Request
from utils.tools import try_catch, get_input_data
from controller.products.products import ProductManager
from middleware.verify_token_route import VerifyTokenRouter


product_route = APIRouter(route_class=VerifyTokenRouter)
product = ProductManager()

@product_route.get('/api/products')
@try_catch
async def get_product(request:Request):
    data = await get_input_data(request)
    return product.get_product(data)
    

@product_route.post('/api/products')
@try_catch
async def create_product(request:Request):
    data = await get_input_data(request)
    return product.create_product(data)