from fastapi import APIRouter


productRoute = APIRouter()


@productRoute.get("/")
def getProducts():
    return {
        "message" : "All Product"
    }