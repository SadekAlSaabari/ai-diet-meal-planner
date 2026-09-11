from fastapi import FastAPI
from agents.diet_agent import DietAgent
from agents.inventory_agent import InventoryAgent
from models import InventoryInput, InventoryResponse, DietInput, DietResponse

# FastAPI istance defining routes and handling HTTP requests
app = FastAPI(title="AI Diet and Meal Planner")

# initialise agents to then be used in the inventory and diet endpoints
inventory_agent = InventoryAgent()
diet_agent = DietAgent()

# root endpoint returning a success message indicating the server is activated
@app.get("/")
async def health_check():
    return {"message": "Success!"}

# inventory endpoint taking a list of items as input and returning a list of usable ingredients and brief confirmation message
@app.post("/inventory", response_model= InventoryResponse)
async def inventory_request(user_input: InventoryInput) -> InventoryResponse:
    result = inventory_agent.run(user_input=user_input)
    return result

# diet endpoint taking a list of ingredients and a preferred diet, then returning items suitable for the diet along with 5 recipe ideas
@app.post("/diet", response_model=DietResponse)
async def diet_request(user_input: DietInput) -> DietResponse:
    result = diet_agent.run(user_input=user_input)
    return result