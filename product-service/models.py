from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, String, Boolean, DateTime, Float, Integer,Text, Enum, text, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy import event
import uuid

Base = declarative_base()


ProductOnCategory = Table(
    "product_detail",
    Base.metadata,
    Column("category_id",String(50), ForeignKey("category.categoryID"),primary_key=True),
    Column("product_id",String(50), ForeignKey("product.productID"), primary_key=True)
)


class Product(Base):
    __tablename__ = "product"
    productID = Column(String(50), primary_key=True, autoincrement=False)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text,nullable=True)
    isFavorite=Column(Boolean, default=False)
    isFlashSale = Column(Boolean, default=False)
    discount = Column(Float,nullable=True)
    discount_type = Column(Enum("currency", "percentage",name="discount_type"), nullable=True)
    likes = Column(Integer, default=0)
    image = Column(String(255), nullable=True)
    owner = Column(String(255), nullable=False)
    productLegal = Column(String(255), nullable=True)
    tags = Column(String(255), nullable=True)
    quantity = Column(Integer, nullable=False)
    createdAt = Column(DateTime, server_default=text("NOW()"))
    updatedAt = Column(DateTime, server_onupdate=text("NOW()"))
    product_category_id = relationship("Category",  secondary=ProductOnCategory ,back_populates="category_id")

    def __init__(self, name, price,description, isFavorite, isFlashSale, discount,discount_type,image,owner,productLegal,tags,quantity, likes = 0):
        self.name = name
        self.price = price
        self.description = description
        self.isFavorite = isFavorite
        self.isFlashSale = isFlashSale
        self.discount =discount
        self.discount_type = discount_type
        self.likes = likes
        self.image = image
        self.owner = owner
        self.productLegal = productLegal
        self.tags = tags
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"{self.name} {self.price} {self.quantity} {self.description} {self.isFavorite} {self.isFlashSale} {self.discount} {self.discount_type} {self.likes} {self.image} {self.owner} {self.productLegal} {self.tags}" 


@event.listens_for(Product, "before_insert")
def productIDToUUID(mapper,connection,target):
    target.productID = uuid.uuid4()


class Category(Base):
    __tablename__  = "category"
    categoryID = Column(String(50), primary_key=True, autoincrement=False)
    name = Column(String(100), unique=True)
    createdAt = Column(DateTime, server_default=text("NOW()"))
    category_id = relationship("Product", secondary=ProductOnCategory, back_populates="product_category_id")

    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return f"{self.name} {self.categoryID} {self.createdAt}"


@event.listens_for(Category, "before_insert")
def productIDToUUID(mapper,connection,target):
    target.categoryID = uuid.uuid4()


