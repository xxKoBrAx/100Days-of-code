#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData

datamanager = DataManager()
flightdata = FlightData()

sheet_data = datamanager.data

for city in sheet_data:
    city["iataCode"] = flightdata.get_iata(city)
    flight_data = flightdata.search_flight(city["iataCode"])
    price = [item["price"][0] for item in flight_data]
    departure_city_name = [item["cityFrom"][0] for item in flight_data]
    departure_iata_airport = [item["flyFrom"][0] for item in flight_data]
    arrival_city_name = [item["cityTo"][0] for item in flight_data]
    iata_city_to = [item["flyTo"][0] for item in flight_data]
    outbound_data = [str(item["local_departure"][0]).strip("T") for item in flight_data]
    inbound_data = [str(item["local_arrival"][0]).strip("T") for item in flight_data]
    if city["LowerPrice"] < price:
        print(f"Low Price Alert!\nOnly {price}£ to fly from {departure_city_name}-{departure_iata_airport} to {arrival_city_name}-{iata_city_to},\n from {outbound_data} to {inbound_data}")

