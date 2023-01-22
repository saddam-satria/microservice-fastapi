from database import session
from models import Product, Category


def getProductByID(productID):
    return session.query(Product).filter(Product.productID == productID).first()

def getProductByQuery(query : str) -> list:
    return session.query(Product).filter((Product.name.like(f"%{query}%") ) | (Product.tags.like(f"%{query}%") | (Product.owner.like(f"%{query}%") | (Category.name == query))) ).all()


def getCategoryByName(categoryName: str):
    return session.query(Category).filter(Category.name == categoryName).first()

def getCategoryByID(categoryID: str):
    return session.query(Category).filter(Category.categoryID == categoryID).first()
