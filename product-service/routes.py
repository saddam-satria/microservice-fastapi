from fastapi import APIRouter
from database import session
from models import Product
from helpers.response import getReponse
from schemas import ProductSchema
productRoute = APIRouter()


@productRoute.get("/")
def getProducts():
    products = session.query(Product).all()
    return getReponse(data=products, serviceName="get all products")



@productRoute.post("/")
def insertProduct(productData : ProductSchema):
    return getReponse(data=None, serviceName="post product",payload=productData)
