from agents.travel_agent import generate_travel_guide
from agents.food_agent import generate_food_recommendations
from agents.weather_agent import generate_weather_info
from agents.budget_agent import generate_budget_plan
from agents.itinerary_agent import generate_itinerary

def generate_complete_report(destination, days, budget):
    # 1. Fetch data from all your sub-agents
    travel = generate_travel_guide(destination)
    food = generate_food_recommendations(destination)
    weather = generate_weather_info(destination)
    itinerary = generate_itinerary(destination, days)
    budget_plan = generate_budget_plan(destination, budget)

    # 2. Build the final clean report block
    report = f"""
# Travel Guide for {destination}
{travel}

# Food Recommendations
{food}

# Weather Information
{weather}

# Budget Plan
{budget_plan}

# {days}-Day Itinerary
{itinerary}
"""

    return report