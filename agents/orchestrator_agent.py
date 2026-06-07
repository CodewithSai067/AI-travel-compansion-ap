from agents.travel_agent import generate_travel_guide
from agents.food_agent import recommend_food
from agents.weather_agent import weather_advice
from agents.itinerary_agent import generate_itinerary

def generate_complete_report(destination, days):

    travel = generate_travel_guide(destination)
    food = recommend_food(destination)
    weather = weather_advice(destination)
    itinerary = generate_itinerary(destination, days)

    report = f"""
# Travel Guide

{travel}

# Food Recommendations

{food}

# Weather Information

{weather}

# {days}-Day Itinerary

{itinerary}
"""

    return report