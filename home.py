import location_images
from prompt1 import suggest_destinations, get_itinerary
import streamlit as st
from datetime import datetime, timedelta


# Set page config
st.set_page_config(
    page_title="Rogue Traveler",
    page_icon="✈️",
    layout="wide"
)

# App title and description
st.title("✈️ Rogue Traveler")
st.markdown("Your AI-powered travel companion for Rogue trip planning!")
if 'open_ai_key' not in st.session_state:
    st.session_state['open_ai_key'] = ""
if 'google_search_key' not in st.session_state:
    st.session_state['google_search_key'] = ""


@st.fragment()
def onclick_details(index, destination):
    if st.button("details", key=f"city_details_{index}"):
        st.write(get_itinerary(destination, start_date, end_date, budget, origin_city))

@st.dialog("Please enter your required keys")
def input_keys():
    open_ai_key = st.text_input("Enter your OpenAI key here...")
    google_search_key = st.text_input("Enter your Google Search key here...")
    if st.button("Submit"):
        st.session_state.open_ai_key = open_ai_key
        st.session_state.google_search_key = google_search_key
        st.rerun()
    

# Sidebar for user inputs
with st.sidebar:
    st.header("Trip Details")
    
    # Origin city input
    origin_city = st.text_input("Origin City", placeholder="e.g. Seattle, WA", value="Seattle, WA")
    
    # Budget input
    budget = st.number_input("Budget (USD)", min_value=0, step=100, value=1000)

    rogueness = st.slider("Rogueness", min_value=0, max_value=10, value=5)
    
    # Date inputs
    start_date = st.date_input("Start Date", min_value="today")
    end_date = st.date_input("End Date", min_value=start_date + timedelta(days=3))

    generate = st.button("Generate Trip Plan", key="generate")

# Main content area
if origin_city and budget and start_date and end_date:
    duration = (end_date - start_date).days
    if duration <= 0:
        st.error("End date must be after start date!")
    else:

        if generate:
            if st.session_state["open_ai_key"] != "":
                try:
                    with st.spinner("Planning your perfect trip..."):
                        # Call the API endpoint and return a JSON object
                        suggestions = suggest_destinations(origin_city)

                        for i in range(len(suggestions['destinations'])):
                            with st.container(border=True):
                                destination = suggestions.get('destinations')[i].get('location')
                                st.write(destination)
                                
                                imageUrl = location_images.get_image(searchstring=destination);
                                st.image(imageUrl, caption=destination)
                                st.write(suggestions.get('destinations')[i].get('description'))
                                onclick_details(i,destination)

                    
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                input_keys() # if the keys are not initialized, open the dialog for user to input
else:
    st.info("Please fill in all the trip details in the sidebar to get started!")



# Footer
st.markdown("---")
st.markdown("Made by WayFinder")