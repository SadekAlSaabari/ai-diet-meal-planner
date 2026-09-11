from pydantic import BaseModel
from typing import List

class InventoryResponse(BaseModel):
    usable_items: List[str]
    message: str

class DietResponse(BaseModel):
    compatible_items: List[str]
    suggested_recipe_ideas: List[str]

class ManagerResponse(BaseModel):
    usable_items: List[str]
    diet_filtered: List[str]
    suggestions: List[str]

class InventoryInput(BaseModel):
    items: List[str]

class DietInput(BaseModel):
    items: List[str]
    diet: str

class ManagerInput(BaseModel):
    items: List[str]
    diet: str

class RecipePlanInput(BaseModel):
    base_recipe: str

class RecipeRecommendInput(BaseModel):
    items: List[str]
    diet: str
    recipe_count: int = 5

class RecipeStep(BaseModel):
    step_number: int
    instruction: str

class RecipeResponse(BaseModel):
    title: str
    ingredients: List[str]
    steps: List[RecipeStep]

class RecipeGroupResponse(BaseModel):
    recipes: List[RecipeResponse]