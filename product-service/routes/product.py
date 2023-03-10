from fastapi import APIRouter, HTTPException,status
from database import session,engine
from models import Product,Category
from helpers.response import getReponse
from schemas import ProductSchema, ProductSchemaUpdate
from repository import getProductByID,getProductByQuery,getCategoryByName
import datetime
from sqlalchemy import text

productRoute = APIRouter()


@productRoute.get("/")
def getProducts(q = None):
    products = engine.execute('select product.*, category.name as category, category."categoryID" from product_detail INNER JOIN product ON product."productID"=product_detail.product_id INNER JOIN category ON product_detail.category_id = category."categoryID" ').all()
    totalProduct = session.query(Product).count()
    if q:
        products = getProductByQuery(q)

    return getReponse(data=products, serviceName="get all products" ,totalData=totalProduct)

@productRoute.post("/")
def insertProduct(productData : ProductSchema):
    newProduct = Product(name=productData.name,price=productData.price,quantity=productData.quantity,description=productData.description,isFavorite=productData.isFavorite,isFlashSale=productData.isFlashSale,  discount=productData.discount, discount_type=productData.discount_type,image=productData.image, owner=productData.owner, productLegal=productData.productLegal, tags=productData.tags)
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
    product = engine.execute(text('select product.*, category.name as category, category."categoryID" from product_detail INNER JOIN product ON product."productID"=product_detail.product_id INNER JOIN category ON product_detail.category_id = category."categoryID" where product_detail.product_id = :productid '), {"productid" : productID}).all()
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=getReponse(serviceName="get product", errorMessage="product not found",payload=productID,responseStatus="error", statusCode=status.HTTP_404_NOT_FOUND))
    return getReponse(serviceName="get product", data=product)

@productRoute.put("/{productID}")
def updateProduct(productID, productData : ProductSchemaUpdate):
    product = getProductByID(productID) 
  
    if product is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=getReponse(serviceName="update product", errorMessage="product not found", payload=productID,statusCode=status.HTTP_404_NOT_FOUND, responseStatus="error"))

    product.name = productData.name if productData.name else  product.name
    product.price = productData.price if productData.price else  product.price
    product.owner = productData.owner if productData.owner else  product.owner
    product.description = productData.description if productData.description else  product.description
    product.discount = productData.discount if productData.discount else  product.discount
    product.discount_type = productData.discount_type if productData.discount_type else  product.discount_type
    product.image = productData.image if productData.image else  product.image
    product.isFlashSale = productData.isFlashSale if productData.isFlashSale else  product.isFlashSale
    product.isFavorite = productData.isFavorite if productData.isFavorite else  product.isFavorite
    product.likes = productData.likes if productData.likes else  product.likes
    product.tags = productData.tags if productData.tags else  product.tags
    product.quantity = productData.quantity if productData.quantity else  product.quantity
    product.productLegal = productData.productLegal if productData.productLegal else  product.productLegal
    product.updatedAt = datetime.datetime.now()
  
    if productData.category:
        category = getCategoryByName(productData.category)
        prevCategory = session.query(Category).filter(Category.categoryID ==product.product_category_id[0].categoryID).first()
        if category is None:
            category = Category(productData.category)


        
        product.product_category_id.remove(prevCategory)
        product.product_category_id.append(category)


    session.flush()
    session.commit()
    
   

    return getReponse(serviceName="update product", data=None, payload=productData)
