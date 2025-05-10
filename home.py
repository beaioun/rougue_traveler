import streamlit as st
import openai
from datetime import datetime, timedelta
import os

# Configure OpenAI API using Streamlit secrets
# openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set page config
st.set_page_config(
    page_title="Rogue Traveler",
    page_icon="✈️",
    layout="wide"
)

# App title and description
st.title("✈️ Rogue Traveler")
st.markdown("Your AI-powered travel companion for Rogue trip planning!")

# Sidebar for user inputs
with st.sidebar:
    st.header("Trip Details")
    
    # Origin city input
    origin_city = st.text_input("Origin City", placeholder="e.g., New York")
    
    # Budget input
    budget = st.number_input("Budget (USD)", min_value=0, step=100, value=1000)
    
    # Date inputs
    start_date = st.date_input("Start Date", min_value=datetime.now().date())
    end_date = st.date_input("End Date", min_value=start_date)

    generate = st.button("Generate Trip Plan", key="generate")

# Main content area
if origin_city and budget and start_date and end_date:
    # Calculate trip duration
    duration = (end_date - start_date).days
    
    if duration <= 0:
        st.error("End date must be after start date!")
    else:
        # Prepare the prompt for OpenAI
        if generate:
            prompt = f"""
            
            """
            
            try:
                with st.spinner("Planning your perfect trip..."):
                    # Call OpenAI API
                    response = openai.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a knowledgeable travel agent with expertise in budget travel planning."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    
                    # Display the response
                    st.markdown("### Your Personalized Travel Plan")
                    st.write(response.choices[0].message.content)
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
else:
    st.info("Please fill in all the trip details in the sidebar to get started!")

# Footer
st.markdown("---")
st.markdown("Made by Rogue Traveler") 