from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
import os

open_key = "INSERT API KEY HERE"
# Create an llm object to use for the QueryEngine and the ReActAgent
llm = OpenAI(model="gpt-4o-mini", api_key=open_key)

origin_location = "Seattle"
number_of_locs = 5

locationgen_str = f"""You are a travel location planner agent. You are going to build a list of travel destinations from the {origin_location} for the user that is looking for an off-the-beaten-path travel destination to travel to and wants to go rogue.

Create a list of {number_of_locs} output travel destinations (town/city), the airport codes for the nearest international airport, a short description of the location, and some tags (eg. wildlife) associated to the location and provide them in JSON format. DO NOT PROVIDE ANY ADDITIONAL TEXT OUTSIDE THE JSON FILE.

Consider the details of the location required to be based on the follows:
Rogue Place Definition:
Location - (destination city/town)
Uncommon/remote place
Not too adventurous
Examples of travel destinations are:
Winthrop, WA
Astoria, Oregon
Rodeo, Kansas City"""

response_locations = llm.complete(prompt = locationgen_str, response_format={ "type": "json_object" })