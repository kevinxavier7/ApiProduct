from database.database import Database
from models.product import Product
from utils.tools import response, response_error
from fastapi import status
from schemas.productvalidation import CreateProduct

class ProductManager:
    def __init__(self):
        self.db = Database()
        
    def get_product(self, data=None):
        
        if data is None:
            product = self.db.get_all(Product)
        else:
            product = self.db.get(Product, Product.product_id == data['product_id'])
            if not product:                
                return response_error("product not found", status.HTTP_404_NOT_FOUND)  
        return response("list products", product, status.HTTP_200_OK)     
    
    
    def create_product(self, data:dict):       
        
        request = CreateProduct(**data)
        
        if request.validate:
            self.db.add(Product,data)
            return response(
                "product created successfully",
                data,
                status.HTTP_201_CREATED
            )
        