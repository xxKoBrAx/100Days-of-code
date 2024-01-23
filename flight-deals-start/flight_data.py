import requests
import datetime

class FlightData:

    def __init__(self):
        self.api_key = "**********"
        self.endpoint = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": self.api_key
        }

    def get_iata(self, city):
        self.get_endpoint = f"{self.endpoint}/locations/query"
        self.params = {
            "term": city["city"]
        }
        self.response = requests.get(url=self.get_endpoint, params=self.params, headers=self.headers)
        self.result = self.response.json()
        return self.result["locations"][0]["code"]

    def search_flight(self, city):
        date_from = datetime.datetime.now().strftime("%d/%m/%Y")
        date_to = (datetime.datetime.today() + datetime.timedelta(6 * 30)).strftime("%d/%m/%Y")
        return_from = (datetime.datetime.today() + datetime.timedelta(7)).strftime("%d/%m/%Y")
        return_to = (datetime.datetime.today() + datetime.timedelta(28)).strftime("%d/%m/%Y")
        self.search_endpoint = f"{self.endpoint}/v2/search"
        self.params = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": date_from,
            "date_to": date_to,
            "return_from": return_from,
            "return_to": return_to,
            "curr": "GBP",
            "max_stopovers": 0,
            }
        self.response = requests.get(url=self.search_endpoint, params=self.params, headers=self.headers)
        self.result = self.response.json()
        print(self.result["data"])

        #print(self.result["data"])
