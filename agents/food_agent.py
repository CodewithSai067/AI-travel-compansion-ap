from backend.config import model

def generate_food_recommendations(destination):
    prompt = f"Give a complete local food and restaurant guide for {destination}."
    response = model.generate_content(prompt)
    return response.text