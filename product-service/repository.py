from database import session
from models import Product


def getProductByID(productID):
    return session.query(Product).filter(Product.productID == productID).first()

def getProductByQuery(query : str) -> list:
    return session.query(Product).filter((Product.name.like(f"%{query}%") ) | (Product.category == query )| (Product.tags.like(f"%{query}%") | (Product.owner.like(f"%{query}%"))) ).all()