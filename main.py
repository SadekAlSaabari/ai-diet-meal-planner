from fastapi import FastAPI
from agents.diet_agent import DietAgent
from agents.inventory_agent import InventoryAgent
from agents.manager_agent import ManagerAgent
from models import InventoryInput, InventoryResponse, DietInput, DietResponse, ManagerInput, ManagerResponse

# FastAPI istance defining routes and handling HTTP requests
app = FastAPI(title="AI Diet and Meal Planner")

# initialise agents to then be used in the inventory and diet endpoints
inventory_agent = InventoryAgent()
diet_agent = DietAgent()
manager_agent = ManagerAgent()

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
    result = manager_agent.run(user_input=user_input)
    return result