from models import RecipePlanInput, RecipeRecommendInput, RecipeResponse, RecipeGroupResponse, ManagerInput
from services.llm_client import LLMClient
from agents.manager_agent import ManagerAgent

system_prompt = (
    f"You are a recipe planning agent. Given a JSON object containing the name of a dish, generate a step-by-step recipe of how to prepare the dish. This must be returned as a structured JSON object with:\n"
    "  title: a single string of the dish's name,\n"
    "  ingredients: an array of the ingredients needed to prepare the dish.\n"
    "  steps: an array of steps that are each made up of two elements:\n"
    "    step_number: an integer with each step being given a step number in order starting from 1,\n"
    "    instruction: a string detailing what to do in that step of the recipe.\n"
    "Respond ONLY with valid JSON."
)

class PlannerAgent:
    def __init__(self):
        self.llm = LLMClient()

    def planRecipe(self, user_input: RecipePlanInput) -> RecipeResponse:
        prompt = f"Dish: {user_input.base_recipe}. Please generate the recipe for it in the structure specified in the system prompt."

        output = self.llm.call_model_json(prompt=prompt, system_prompt=system_prompt)

        result = RecipeResponse(**output)
        return result

    def recommend(self, user_input: RecipeRecommendInput) -> RecipeGroupResponse:
        user_items = user_input.items
        user_diet = user_input.diet
        organised_input = ManagerInput(items=user_items, diet=user_diet)

        recipe_manager = ManagerAgent()
        manager_output = recipe_manager.run(organised_input)

        recipe_list = []

        for i in range(user_input.recipe_count):
            this_dish = manager_output.suggestions[i]
            this_recipe = self.planRecipe(user_input=RecipePlanInput(base_recipe=this_dish))
            recipe_list.append(this_recipe)

        result = RecipeGroupResponse(recipes=recipe_list)
        return result


