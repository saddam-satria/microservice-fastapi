from fastapi import APIRouter, HTTPException,status
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
    newProduct = Product(name=productData.name,price=productData.price,description=productData.description,isFavorite=productData.isFavorite,isFlashSale=productData.isFlashSale, category=productData.category, discount=productData.discount, discount_type=productData.discount_type,image=productData.image, owner=productData.owner, productLegal=productData.productLegal, tags=productData.tags)

    session.add(newProduct)
    session.commit()
    return getReponse(data=None, serviceName="post product",payload=productData)

@productRoute.delete("/{productID}")
def deleteProduct(productID):
    product = getProductByID(productID)

    if product == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=getReponse(serviceName="delete product", errorMessage="product not found", payload=productID,statusCode=404))


    session.delete(product)
    session.commit()
    return getReponse(serviceName="delete product")



def getProductByID(productID):
    return session.query(Product).filter(Product.productID == productID).first()