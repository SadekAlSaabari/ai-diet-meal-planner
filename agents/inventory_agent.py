from services import llm_client
from models import InventoryInput, InventoryResponse

# system prompt for inventory model
system_prompt = (
            f"You are a kitchen assistant. Given a JSON array of ingredients, return a JSON object with:\n"
            "  usable_items: an array of ingredients that are non-empty and suitable for cooking (remove blank or invalid entries),\n"
            "  message: a short confirmation string.\n"
            "Respond ONLY with valid JSON."
        )

class InventoryAgent:
    def __init__(self):
        self.llm = llm_client.LLMClient()

    def run(self, user_input: InventoryInput) -> InventoryResponse:
        collected_items = f"Please clean this list of ingredients: {user_input.items})"

        model_output = self.llm.call_model_json(prompt=collected_items, system_prompt=system_prompt)

        return InventoryResponse(**model_output)
