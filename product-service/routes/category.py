from fastapi import APIRouter,status
from helpers.response import getReponse
from database import session
from models import Category


categoryRoute = APIRouter(prefix="/product/category")



@categoryRoute.get("/")
def getCategories():
    categories = session.query(Category).all()
    return getReponse(serviceName="get categories", data=categories, statusCode=status.HTTP_200_OK)