# Import Streamlit
import streamlit as st

# Title of the web app
st.title('User Information Form')

# Form for user input
with st.form("user_info_form"):
    # Text input for name
    name = st.text_input('Name')

    # Number input for age (you can adjust min_value and max_value as needed)
    age = st.number_input('Age', min_value=1, max_value=100)

    # Form submit button
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Hello, {name}! You are {age} years old.")

# Run the following command in your terminal to start the Streamlit app:
# streamlit run app.py
