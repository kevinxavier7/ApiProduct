from fastapi import FastAPI
from routers.userouter import user_router
from routers.login import login_router
from routers.product import product_route


app = FastAPI()


app.include_router(user_router)
app.include_router(login_router)
app.include_router(product_route)

    

