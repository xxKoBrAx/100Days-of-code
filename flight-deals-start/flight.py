from ryanair import Ryanair
from datetime import datetime, timedelta
from ryanair.types import Flight

api = Ryanair(currency="EUR")
tomorrow = datetime.today().date() + timedelta(days=1)
flights = api.get_cheapest_flights("PMO", tomorrow, tomorrow + timedelta(days=1))


flight: Flight = flights[0]
print(flight)  
print(flight.price) 
