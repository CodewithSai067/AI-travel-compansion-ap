from backend.config import model

def generate_weather_info(destination):

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