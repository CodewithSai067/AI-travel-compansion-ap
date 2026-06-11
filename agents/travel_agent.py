import config 
model = config.model

def generate_travel_guide(destination):

    prompt = f"""
    Give a complete travel guide for {destination}.

    Include:
    - Tourist attractions
    - Local foods
    - Best time to visit
    - Travel tips
    """

    response = model.generate_content(prompt)

    return response.text