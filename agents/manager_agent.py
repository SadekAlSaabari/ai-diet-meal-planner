from agents.diet_agent import DietAgent
from agents.inventory_agent import InventoryAgent
from models import DietInput, InventoryInput, ManagerInput, ManagerResponse

class ManagerAgent():
    def __init__(self):
        self.inventory = InventoryAgent()
        self.diet = DietAgent()

    def run(self, user_input: ManagerInput) -> ManagerResponse:
        inventory_result = self.inventory.run(user_input=InventoryInput(items=user_input.items))

        packaged_diet_input = DietInput(items=inventory_result.usable_items, diet=user_input.diet)

        diet_result = self.diet.run(user_input=packaged_diet_input)

        final_result = ManagerResponse(
            usable_items=inventory_result.usable_items,
            diet_filtered=diet_result.compatible_items,
            suggestions=diet_result.suggested_recipe_ideas
        )
        return final_result