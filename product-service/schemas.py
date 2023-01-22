from pydantic import BaseModel

class ProductSchema(BaseModel):
    name : str 
    price : float
    description : str = None
    isFavorite : bool = False
    isFlashSale : bool = False
    category: str 
    discount: float = None
    discount_type: str = None
    likes: int = 0
    image : str = None
    owner: str 
    productLegal : str = None
    tags : str= None
    quantity : int = 0

class ProductSchemaUpdate(ProductSchema):
    name : str = None 
    price : float = None 
    description : str = None 
    isFavorite : bool = False 
    isFlashSale : bool = False
    category : str = None 
    discount : float = None 
    discount_type : str = None 
    image : str = None 
    owner : str = None 
    productLegal : str = None
    tags : str = None
