import os
import requests
from pprint import pprint

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv('SERP_API_KEY')

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        flight_search_endpoint = "https://serpapi.com/search"
        flight_search_parameters = {
          "engine": "google_flights",
          "departure_id": origin_city_code,
          "arrival_id": destination_city_code,
          "outbound_date": from_time,
          "return_date": to_time,
          "type": "1",
          "adults": "1",
          "currency": "USD",
          "api_key": self._api_key,
         }
        return requests.get(url=flight_search_endpoint, params=flight_search_parameters).json()
