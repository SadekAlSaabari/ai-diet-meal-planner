from services import llm_client
from models import DietInput, DietResponse

# system prompt for inventory model
system_prompt = (
            f"You are a diet-friendly meal planner. Given a JSON list of ingredients and a specified diet, return a JSON object with:\n"
            "  compatible_items: an array of ingredients that are suitable for the user's dietary requirements,\n"
            "  suggested_recipe_ideas: a list of EXACTLY 5 ideas for dishes that could be made with the compatible items available.\n"
            "Respond ONLY with valid JSON."
        )

class DietAgent:
    def __init__(self):
        self.llm = llm_client.LLMClient()

    def run(self, user_input: DietInput) -> DietResponse:
        user_prompt = (f"Ingredients: {user_input.items}\n"
            f"Diet: {user_input.diet}\n"
            "Please filter the ingredients and provide exactly 5 suggested recipe ideas.")

        model_output = self.llm.call_model_json(prompt=user_prompt, system_prompt=system_prompt)

        return DietResponse(**model_output)