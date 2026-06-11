from backend.config import model

def recommend_food(destination):

    prompt = f"""
    Recommend famous local foods in {destination}.

    Include:
    - Traditional dishes
    - Popular street foods
    - Famous desserts
    - Must-try restaurants
    """

    response = model.generate_content(prompt)

    return response.text