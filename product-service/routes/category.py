from fastapi import APIRouter,status,HTTPException
from helpers.response import getReponse
from database import session
from models import Category
from repository import getCategoryByID

categoryRoute = APIRouter(prefix="/product/category")



@categoryRoute.get("/")
def getCategories():
    categories = session.query(Category).all()
    return getReponse(serviceName="get categories", data=categories, statusCode=status.HTTP_200_OK)

@categoryRoute.get("/{categoryID}")
def getCategories(categoryID : str):
    category = getCategoryByID(categoryID)
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=getReponse(serviceName="get category", errorMessage="category not found", payload=categoryID,statusCode=status.HTTP_404_NOT_FOUND, responseStatus="error"))

    return getReponse(serviceName="get category", data=category, statusCode=status.HTTP_200_OK)