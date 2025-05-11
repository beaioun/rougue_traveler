import arrow
import json

text_json = json.loads(response.text)

time_now = arrow.utcnow()
future_time = time_now.shift(days=30)

origin_location = "SEA"
destination = "PDX"

try:
  flight_info = amadeus.shopping.flight_offers_search.get(
                  originLocationCode=origin_location,
                  destinationLocationCode=destination,
                  departureDate=future_time.format('YYYY-MM-DD'),
                  adults=1
                )
except ResponseError as error:
  raise error

flights_for_destinations = flight_info.data
flights = []
for flight in flights_for_destinations:
    flight_info = {
      "id": flight["id"],
      "price": {
          "currency": flight["price"]["currency"],
          "total": flight["price"]["total"],
          "base": flight["price"]["base"]
      },
      "number_of_bookable_seats": flight["numberOfBookableSeats"],
      "validating_airline_codes": flight["validatingAirlineCodes"],
      "itineraries": []
    }
    for itinerary in flight["itineraries"]:
      itinerary_info = {
          "duration": itinerary["duration"],
          "segments": []
      }

      for segment in itinerary["segments"]:
          segment_info = {
              "departure_airport": segment["departure"]["iataCode"],
              "departure_time": segment["departure"]["at"],
              "arrival_airport": segment["arrival"]["iataCode"],
              "arrival_time": segment["arrival"]["at"],
              "carrier_code": segment["carrierCode"],
              "flight_number": segment["number"],
              "duration": segment["duration"],
              "number_of_stops": segment["numberOfStops"]
          }
          itinerary_info["segments"].append(segment_info)

      flight_info["itineraries"].append(itinerary_info)

    flights.append(flight_info)

print(json.dumps(flights, indent=2))

