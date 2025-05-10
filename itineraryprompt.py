destination_hc = "Winthrop, WA"
start_date_hc = "2025-07-01"
end_date_hc = "2025-07-07"
budget_hc = 1000
no_of_days_hc = 5
origin_location_hc = "Seattle, WA"

itinerary_planning_prompt = f"""You are a travel planning agent. You are going to build a travel package for the user that is looking for an off-the-beaten-path travel to travel to {destination_hc} and wants to go rogue.

The travel package should include an itinerary for what to do there based on the activities to do within the place. Consider the travel start date {start_date_hc} and end date {end_date_hc}, and the budget {budget_hc} and origin location {origin_location_hc} in defining the number of days available for the actual travel experience within the location.

Consider the details required to be based on the follows:
- Activities within the place are Unique and not touristy/popular
- Traveler is Solo

Generate the output to include the following details in the itinerary: such as the details of the activities, their asosciated costs, and the total cost of the travel package. Provide them in JSON format. DO NOT PROVIDE ANY ADDITIONAL TEXT OUTSIDE THE JSON FILE.

"""

response_itinerary = llm.complete(prompt = itinerary_planning_prompt)