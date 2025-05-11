from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
import streamlit as st
import json
@st.cache_resource()
def get_llm():
    open_ai_key = st.session_state.open_ai_key
    llm = OpenAI(model="gpt-4o-mini", api_key=open_ai_key)
    return llm

@st.cache_data()
def suggest_destinations(origin_location):
    # Set up the OpenAI API key
    # open_key = os.getenv("OPENAI_API_KEY")
    # For testing purposes, you can set the API key directly
    #
    number_of_locs = 5
    # open_key = keys.open_api_key
    # # Create an llm object to use for the QueryEngine and the ReActAgent
    # llm = OpenAI(model="gpt-4o-mini", api_key=open_key)
    
    locationgen_str = f"""You are a travel location planner agent. You are going to build a list of travel destinations from the {origin_location} for the user that is looking for an off-the-beaten-path travel destination to travel to and wants to go rogue.

    Create a list of {number_of_locs} output travel destinations (town/city), the airport codes for the nearest international airport, a short description of the location, and some tags (eg. wildlife) associated to the location and provide them in JSON format. DO NOT PROVIDE ANY ADDITIONAL TEXT OUTSIDE THE JSON FILE.

    Consider the details of the location required to be based on the follows:
    Rogue Place Definition:
    Location - (destination city/town)
    Uncommon/remote place
    Not too adventurous
"""
    llm = get_llm()
    response = llm.complete(prompt = locationgen_str, response_format={ "type": "json_object" })
    response_json = json.loads(response.text)
    return response_json

@st.cache_data()
def get_itinerary(destination, start_date, end_date, budget, origin_location):
    
    itinerary_planning_prompt = f"""You are a travel planning agent. You are going to build a travel package for the user that is looking for an off-the-beaten-path travel to travel to {destination} and wants to go rogue.

    The travel package should include an itinerary for what to do there based on the activities to do within the place. Consider the travel start date {start_date} and end date {end_date}, and the budget {budget} and origin location {origin_location} in defining the number of days available for the actual travel experience within the location.

    Consider the details required to be based on the follows:
    - Activities within the place are Unique and not touristy/popular
    - Traveler is Solo

    Generate the output to include the following details in the itinerary: such as the details of the activities, their asosciated costs, and the total cost of the travel package. Provide them in JSON format. DO NOT PROVIDE ANY ADDITIONAL TEXT OUTSIDE THE JSON FILE.

    """
    llm = get_llm()
    response_locations = llm.complete(prompt = itinerary_planning_prompt, response_format={ "type": "json_object" })
    response_json = json.loads(response_locations.text)
    itinerary = response_json.get('travel_package').get('itinerary')
    return itinerary
