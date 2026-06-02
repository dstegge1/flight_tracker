import os
from requests.auth import HTTPBasicAuth
import requests
from pprint import pprint

class DataManager:
    def __init__(self):
        self.username = os.environ.get("SHEETY_USERNAME")
        self.password = os.environ.get("SHEETY_PASSWORD")
        self.get_endpoint = "https://api.sheety.co/4187912d679c992e84911d466be33df2/flightDeals/prices"
        self.sheety_headers = {
            "Authorization": "Basic bnVsbDpudWxs"
        }
        self.sheety_basic_auth = HTTPBasicAuth(username=self.username, password=self.password)
    def get_destination_data(self, iata_code):
        sheety_response = requests.get(url=self.get_endpoint, headers=self.sheety_headers,
                                       auth=self.sheety_basic_auth).json()
        sheet_price = 0
        for section in sheety_response["prices"]:
            if section["iataCode"] == iata_code:
                sheet_price = section["lowestPrice"]
        return sheet_price
    def get_index(self, iata_code):
        sheety_response = requests.get(url=self.get_endpoint).json()
        index = 1
        for section in sheety_response["prices"]:
            index += 1
            if section["iataCode"] == iata_code:
                print(f"Index: {index}")
                return index
    def update_lowest_price(self, new_price, iata_code):
        index = self.get_index(iata_code=iata_code)
        sheety_put_endpoint = f"{self.get_endpoint}/{index}"
        sheet_inputs = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(sheety_put_endpoint, json=sheet_inputs)
        print(response.json())
        response.raise_for_status()
