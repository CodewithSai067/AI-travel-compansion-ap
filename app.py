import streamlit as st
import requests

st.title("🌍 AI Travel Companion")

API_URL = "https://ai-travel-companion-496731521484.asia-south1.run.app"

destination = st.text_input("Enter a destination")

days = st.number_input(
    "Number of Days",
    min_value=1,
    max_value=14,
    value=3
)

if st.button("Generate Complete Guide"):
    if destination:
        try:
            response = requests.post(
                f"{API_URL}/generate",
                json={
                    "destination": destination,
                    "days": days
                }
            )

            result = response.json()

            st.write(result)

        except Exception as e:
            st.warning("⚠️ AI service unavailable.")
            st.expander("Technical Details").write(str(e))

    else:
        st.warning("Please enter a destination.")