from config import model

def weather_advice(destination):

    prompt = f"""
    Provide weather information for {destination}.

    Include:
    - Typical climate
    - Best season to visit
    - What clothes to pack
    - Weather-related travel tips
    """

    response = model.generate_content(prompt)

    return response.text