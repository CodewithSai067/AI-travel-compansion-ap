import streamlit as st
from agents.orchestrator_agent import generate_complete_report

st.title("🌍 AI Travel Companion")

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
            result = generate_complete_report(destination,days)
            st.write(result)

        except Exception as e:
            st.warning("⚠️ Gemini API quota reached.")

            st.info("""
The AI service is temporarily unavailable because the free Gemini API limit has been reached.

Please try again later.

Meanwhile, here are some travel tips:
• Check local weather before travelling
• Carry essential documents
• Research local food specialties
• Plan transportation in advance
• Keep emergency contacts handy
""")

            st.expander("Technical Details").write(str(e))

    else:
        st.warning("Please enter a destination.")