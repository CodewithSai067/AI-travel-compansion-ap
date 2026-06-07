if st.button("Generate Complete Guide"):

    if destination:

        try:
            result = generate_complete_report(destination)
            st.write(result)

        except Exception as e:
            st.error(
                "Gemini API quota exceeded. Please wait and try again later."
            )

    else:
        st.warning("Please enter a destination.")