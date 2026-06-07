from agents.travel_agent import generate_travel_guide
from agents.food_agent import recommend_food
from agents.weather_agent import weather_advice

def generate_complete_report(destination):

    travel = generate_travel_guide(destination)
    food = recommend_food(destination)
    weather = weather_advice(destination)

    report = f"""
# Travel Guide

{travel}

# Food Recommendations

{food}

# Weather Information

{weather}
"""

    return report