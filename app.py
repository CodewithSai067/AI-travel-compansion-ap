import streamlit as st
from agents.travel_agent import generate_travel_guide

st.title("🌍 AI Travel Companion")

destination = st.text_input("Enter a destination")

if st.button("Generate Travel Guide"):

    if destination:
        result = generate_travel_guide(destination)
        st.write(result)
    else:
        st.warning("Please enter a destination.")