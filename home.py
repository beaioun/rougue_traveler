import location_images
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
    origin_city = st.text_input("Origin City", placeholder="e.g. Seattle, WA")
    
    # Budget input
    budget = st.number_input("Budget (USD)", min_value=0, step=100, value=1000)

    rogueness = st.slider("Rogueness", min_value=0, max_value=10, value=5)
    
    # Date inputs
    start_date = st.date_input("Start Date", min_value=datetime.now().date())
    end_date = st.date_input("End Date", min_value=start_date + timedelta(days=3))

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
                    # Call the API endpoint and the response is a JSON object
                    response = {
                                "destinations": [
                                    {
                                    "location": "Winthrop, WA",
                                    "airport_code": "SEA"
                                    },
                                    {
                                    "location": "Astoria, OR",
                                    "airport_code": "PDX"
                                    },
                                    {
                                    "location": "Rodeo, KS",
                                    "airport_code": "MHK"
                                    },
                                    {
                                    "location": "Sandpoint, ID",
                                    "airport_code": "SFF"
                                    },
                                    {
                                    "location": "Port Townsend, WA",
                                    "airport_code": "SEA"
                                    }
                                ]
                                }
                    
                    for i in range(len(response['destinations'])):
                        with st.container(border=True):
                            st.write(response.get('destinations')[i].values())
                            city_details = st.button("details", key=f"city_details_{i}")
                            imageUrl = location_images.get_image(searchstring=response.get('destinations')[i].get('location'));
                            st.image(imageUrl, caption=response.get('destinations')[i].get('location'))
                    # Display the response
                    if city_details:
                        # TODO: a function to get the itenary for the city
                        st.write(response.get('destinations')[i].values())

                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            
            if st.button("Clear and Start Over"):
                st.rerun()
else:
    st.info("Please fill in all the trip details in the sidebar to get started!")



# Footer
st.markdown("---")
st.markdown("Made by Rogue Traveler") 