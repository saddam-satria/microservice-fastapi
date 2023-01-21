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