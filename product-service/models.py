from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, String, Boolean, DateTime, Float, Integer,Text, Enum, text
import uuid
Base = declarative_base()



class Product(Base):
    __tablename__ = "product"
    productID = Column(String(50), primary_key=True, autoincrement=False)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text,nullable=True)
    isFavorite=Column(Boolean, default=False)
    isFlashSale = Column(Boolean, default=False)
    category = Column(String(150), nullable=False)
    discount = Column(Float,nullable=True)
    discount_type = Column(Enum("currency", "percentage",name="type_of_discount"), nullable=True)
    likes = Column(Integer, default=0)
    image = Column(String(255), nullable=True)
    owner = Column(String(255), nullable=False)
    productLegal = Column(String(255), nullable=True)
    tags = Column(String(255), nullable=True)
    createdAt = Column(DateTime, server_default=text("NOW()"))
    updatedAt = Column(DateTime, server_onupdate=text("NOW()"))

    def __init__(self, name, price,description, isFavorite, isFlashSale, category,discount,discount_type,likes,image,owner,productLegal,tags):
        self.name = name
        self.price = price
        self.description = description
        self.isFavorite = isFavorite
        self.isFlashSale = isFlashSale
        self.category = category
        self.discount =discount
        self.discount_type = discount_type
        self.likes = likes
        self.image = image
        self.owner = owner
        self.productLegal = productLegal
        self.tags = tags
        self.productID = uuid.uuid4()

    def __repr__(self) -> str:
        return f"{self.name} {self.price} {self.description} {self.isFavorite} {self.isFlashSale} {self.category} {self.discount} {self.discount_type} {self.likes} {self.image} {self.owner} {self.productLegal} {self.tags}" 
