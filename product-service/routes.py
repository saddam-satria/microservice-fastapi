from fastapi import APIRouter, HTTPException,status
from database import session
from models import Product,Category
from helpers.response import getReponse
from schemas import ProductSchema, ProductSchemaUpdate
from repository import getProductByID,getProductByQuery,getCategoryByName
import datetime

productRoute = APIRouter()


@productRoute.get("/")
def getProducts(q = None):
    products = session.query(Product).all()

    if q:
        products = getProductByQuery(q)

    return getReponse(data=products, serviceName="get all products")

@productRoute.post("/")
def insertProduct(productData : ProductSchema):
    newProduct = Product(name=productData.name,price=productData.price,description=productData.description,isFavorite=productData.isFavorite,isFlashSale=productData.isFlashSale,  discount=productData.discount, discount_type=productData.discount_type,image=productData.image, owner=productData.owner, productLegal=productData.productLegal, tags=productData.tags)
    category = getCategoryByName(productData.category)
    

    if category is None:
        category = Category(productData.category)

   
    
    newProduct.product_category_id.append(category)
    session.add(newProduct)
    session.commit()
    return getReponse(data=None, serviceName="post product",payload=productData)

@productRoute.delete("/{productID}")
def deleteProduct(productID):
    product = getProductByID(productID)

    if product is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=getReponse(serviceName="delete product", errorMessage="product not found", payload=productID,statusCode=status.HTTP_404_NOT_FOUND, responseStatus="error"))


    session.delete(product)
    session.commit()
    return getReponse(serviceName="delete product")

@productRoute.get("/{productID}")
def getProduct(productID):
    product = getProductByID(productID)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=getReponse(serviceName="get product", errorMessage="product not found",payload=productID,responseStatus="error", statusCode=status.HTTP_404_NOT_FOUND))
    return getReponse(serviceName="get product", data=product)

@productRoute.put("/{productID}")
def updateProduct(productID, productData : ProductSchemaUpdate):
    productFilter = session.query(Product).filter(Product.productID == productID)
    product = productFilter.first()

    if product is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=getReponse(serviceName="update product", errorMessage="product not found", payload=productID,statusCode=status.HTTP_404_NOT_FOUND, responseStatus="error"))

    product = productFilter.update({
        Product.name : productData.name if productData.name else product.name,
        Product.price : productData.price if productData.price else product.price,
        Product.owner : productData.owner if productData.owner else product.owner,
        Product.category : productData.category if productData.category else product.category, 
        Product.description : productData.description if productData.description else product.description,
        Product.discount : productData.discount if productData.discount else product.discount, 
        Product.discount_type : productData.discount_type if productData.discount_type else product.discount_type,
        Product.image : productData.image if productData.image else product.image,
        Product.isFlashSale : productData.isFlashSale if productData.isFlashSale else product.isFlashSale,
        Product.isFavorite : productData.isFavorite if productData.isFavorite else product.isFavorite,
        Product.likes : productData.likes if productData.likes else product.likes,
        Product.tags : productData.tags if productData.tags else product.tags,
        Product.productLegal : productData.productLegal if productData.productLegal else product.productLegal,
        Product.updatedAt : datetime.datetime.now()
    })


    return getReponse(serviceName="update product", data=product, payload=productData)
