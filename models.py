from pydantic import BaseModel
from typing import List

class InventoryResponse(BaseModel):
    usable_items: List[str]
    message: str

class DietResponse(BaseModel):
    compatible_items: List[str]
    suggested_recipe_ideas: List[str]

class InventoryInput(BaseModel):
    items: List[str]

class DietInput(BaseModel):
    items: List[str]
    diet: str