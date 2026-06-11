from config import model

def generate_budget_plan(destination, budget):

    prompt = f"""
    Create a travel budget plan.

    Destination: {destination}
    Budget: ₹{budget}

    Include:
    - Transport
    - Food
    - Stay
    - Activities
    """

    response = model.generate_content(prompt)

    return response.text