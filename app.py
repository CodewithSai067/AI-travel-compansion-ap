import streamlit as st

from agents.travel_agent import generate_travel_guide
from agents.food_agent import recommend_food
from agents.weather_agent import weather_advice

st.title("🌍 AI Travel Companion")

destination = st.text_input("Enter a destination")

if st.button("Generate Complete Guide"):

    if destination:

        st.subheader("🏛 Travel Guide")
        travel_result = generate_travel_guide(destination)
        st.write(travel_result)

        st.subheader("🍽 Food Recommendations")
        food_result = recommend_food(destination)
        st.write(food_result)
        
        st.subheader("🌦 Weather Information")
        weather_result = weather_advice(destination)
        st.write(weather_result)

    else:
        st.warning("Please enter a destination.")