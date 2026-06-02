import requests
from requests.auth import HTTPBasicAuth
import os
import requests_cache
from datetime import datetime, timedelta
import flight_search
from flight_search import FlightSearch
from flight_data import FlightData, find_cheapest_flight
from data_manager import DataManager
from notification_manager import NotificationManager

# set dates
today = datetime.now()
today_date = today.date()
tomorrow = today.replace(day=today.day + 1).date()
six_month_from_today = today.replace(month=today.month + 6).date()
september_departure_date = "2026-09-10"
september_arrival_date = "2026-09-20"

# create parameter variables for flight search
origin_city_code = 'BWI'
destination_city_code = 'HND'

# Get flight data
all_flights = []
fs = FlightSearch()
flight_data_response = fs.check_flights(origin_city_code=origin_city_code, destination_city_code=destination_city_code, from_time=september_departure_date, to_time=september_arrival_date)
cheapest_flight = find_cheapest_flight(flight_data_response, tomorrow)
cheapest_flight_price = cheapest_flight.price
print(f"Cheapest Flight: {cheapest_flight_price}")

# Get FlightSearch Sheets Data
dm = DataManager()
sheet_lowest_price = dm.get_destination_data(destination_city_code)
print(f"Lowest Sheet Price: {sheet_lowest_price}")

# update cheapest price in google sheets if less than one found from api
print(cheapest_flight_price)
if cheapest_flight_price < sheet_lowest_price:
    dm.update_lowest_price(cheapest_flight_price, destination_city_code)
    nf = NotificationManager()
    nf.send_email(destination_city_code, sheet_lowest_price, cheapest_flight_price)
    print("Updated lowest price")
else:
    print("Higher than lowest price on sheet")
