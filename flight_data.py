from pprint import pprint

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
def combine_other_best_flights(data):
    all_flights = []
    try:
        best_flights = data["best_flights"]
        for flight in best_flights:
            all_flights.append(flight)
        try:
            other_flights = data["other_flights"]
        except KeyError:
            print("No Other Flights")
    except KeyError:
        other_flights = data["other_flights"]
        for flight in other_flights:
            all_flights.append(flight)
    return all_flights
def find_cheapest_flight(data, return_date):
    all_flights = combine_other_best_flights(data)
    flight_price_dicts = {}
    lowest_price = 0
    for flight in all_flights:
        origin = flight["flights"][0]["departure_airport"]["id"]
        departure_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
        destination = flight["flights"][-1]["arrival_airport"]["id"]
        price = flight["price"]
        flight_object = FlightData(price=price, origin_airport=origin, destination_airport=destination,
                                   out_date=departure_date, return_date=return_date)
        flight_price_dicts[flight_object] = price
    print(flight_price_dicts)
    cheapest_flight = min(flight_price_dicts, key=flight_price_dicts.get)
    return cheapest_flight
