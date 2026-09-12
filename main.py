from fastapi import FastAPI
from agents.diet_agent import DietAgent
from agents.inventory_agent import InventoryAgent
from agents.manager_agent import ManagerAgent
from agents.planner_agent import PlannerAgent
from models import InventoryInput, InventoryResponse, DietInput, DietResponse, ManagerInput, ManagerResponse, RecipeGroupResponse, RecipeResponse, RecipePlanInput, RecipeRecommendInput
from app.logging import get_logger
import uvicorn

# FastAPI istance defining routes and handling HTTP requests
app = FastAPI(title="AI Diet and Meal Planner")

# initialise agents to then be used in the inventory and diet endpoints
inventory_agent = InventoryAgent()
diet_agent = DietAgent()
manager_agent = ManagerAgent()
planner_agent = PlannerAgent()

# initialise logger
logger = get_logger(name="app")

# root endpoint returning a success message indicating the server is activated
@app.get("/")
async def health_check():
    return {"message": "Success!"}

# inventory endpoint taking a list of items as input and returning a list of usable ingredients and brief confirmation message
@app.post("/inventory", response_model= InventoryResponse)
def inventory_request(user_input: InventoryInput) -> InventoryResponse:
    result = inventory_agent.run(user_input=user_input)
    return result

# diet endpoint taking a list of ingredients and a preferred diet, then returning items suitable for the diet along with 5 recipe ideas
@app.post("/diet", response_model=DietResponse)
def diet_request(user_input: DietInput) -> DietResponse:
    result = diet_agent.run(user_input=user_input)
    return result

# ask endpoint taking a list of items and preferred diet, then using both the inventory and diet agents to return a list of usable items, items compatible with the diet requirement and a list of 5 recipe ideas
@app.post("/ask", response_model=ManagerResponse)
def manager_request(user_input: ManagerInput) -> ManagerResponse:
    logger.info("Received /ask request: items=%s, diet=%s", user_input.items, user_input.diet)
    result = manager_agent.run(user_input=user_input)
    logger.info("/ask response: suggestions=%s", result.suggestions)
    return result

# plan endpoint taking a dish and returning a step by step recipe including ingredients needed and instructions on how to prepare the dish
@app.post("/plan", response_model=RecipeResponse)
def planner_request(user_input: RecipePlanInput) -> RecipeResponse:
    logger.info("Received /plan request: base_recipe=%s", user_input.base_recipe)
    result = planner_agent.planRecipe(user_input=user_input)
    logger.info("/plan response: title=%s", result.title)
    return result

# recommend endpoint taking a list of items and dietary preference, and returning a list of recipe ideas including step by step instructions for each
@app.post("/recommend", response_model=RecipeGroupResponse)
def planner_recommend(user_input: RecipeRecommendInput) -> RecipeGroupResponse:
    logger.info("Received /recommend request: items=%s, diet=%d, recipe_count=%r", user_input.items, user_input.diet, user_input.recipe_count)
    result = planner_agent.recommend(user_input=user_input)
    logger.info("/recommend response: number_of_recipes=%s", len(result.recipes))
    return result