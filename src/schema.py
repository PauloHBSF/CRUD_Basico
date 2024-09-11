from pydantic import BaseModel, PositiveFloat, PositiveInt
from typing import Union

class ItemBase(BaseModel):
    # Validar Input de novo produto do usuário
    name: str
    price: PositiveFloat
    is_offer: Union[bool, None] = None
    
class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: PositiveInt