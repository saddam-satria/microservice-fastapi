from pydantic import BaseModel


class ProductSchema(BaseModel):
    name : str 
    price : float
    description : str 
    isFavorite : bool
    isFlashSale : bool
    category: str 
    discount: float
    discount_type: str 
    likes: int
    image : str
    owner: str 
    productLegal : str 
    tags : str