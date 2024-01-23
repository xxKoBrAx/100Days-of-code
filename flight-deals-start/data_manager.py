import requests

class DataManager:

    def __init__(self):
        self.endpoint = "https://api.sheety.co/e2a2a8c2c5a4ef42ce82913818b2b87a/myFlightDeals/prices"
        self.response = requests.get(url=self.endpoint)
        self.result = self.response.json()
        self.data = self.result["prices"]

    def update_row(self, city):
        self.put_endpoint = f"{self.endpoint}/{city['id']}"
        self.put_params = {
            "price": {
            "iataCode": city["iataCode"]
            }
        }
        self.response = requests.put(url=self.put_endpoint, json=self.put_params)

