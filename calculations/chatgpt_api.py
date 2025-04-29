import requests
import json
import re
def get_food_suggestions(protein, fat, carbohydrates):
    try:
        prompt_text = (
            f"Suggest food ideas and recipes that match approximately "
            f"{protein}g protein, {fat}g fat, and {carbohydrates}g carbohydrates.\n"
            f"Separate them into two categories: 'low_budget' and 'high_budget'.\n"
            f"Return ONLY a valid JSON object with the structure:\n\n"
            f"{{\n"
            f"  \"low_budget\": {{\n"
            f"    \"Food Name 1\": \"Recipe for Food Name 1\",\n"
            f"    \"Food Name 2\": \"Recipe for Food Name 2\"\n"
            f"  }},\n"
            f"  \"high_budget\": {{\n"
            f"    \"Food Name 3\": \"Recipe for Food Name 3\",\n"
            f"    \"Food Name 4\": \"Recipe for Food Name 4\"\n"
            f"  }}\n"
            f"}}\n\n"
            f"No explanations, no extra text. Only valid JSON."
        )

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer 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",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "meta-llama/llama-4-maverick:free",
                "messages": [
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": prompt_text}]
                    }
                ]
            })
        )

        response.raise_for_status()

        response_data = response.json()
        model_content = response_data["choices"][0]["message"]["content"]

        json_match = re.search(r'\{.*\}', model_content, re.DOTALL)
        if not json_match:
            raise ValueError("No valid JSON object found in model response.")

        json_str = json_match.group(0)

        parsed = json.loads(json_str)

        low_budget = parsed.get("low_budget", {})
        high_budget = parsed.get("high_budget", {})

        return low_budget, high_budget

    except Exception as e:
        print(f"An error occurred: {e}")
        return {}, {}

