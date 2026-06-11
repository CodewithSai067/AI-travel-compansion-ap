import config
model = config.model

def generate_itinerary(destination, days):

    prompt = f"""
    Create a detailed {days}-day travel itinerary for {destination}.

    Include:
    - Morning activities
    - Afternoon activities
    - Evening activities
    - Food recommendations
    - Travel tips
    """

    response = model.generate_content(prompt)

    return response.text