from datetime import *
class Event:
    def __init__(self, startTime, endTime, venue):
        self.startTime = startTime
        self.endTime = endTime
        self.venue = venue

class Venue:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Address:
    def __init__(self, street, city, state, country, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode

address = Address("Robson St", "Vancouver", "BC", "Canada", "8X54Y3")
venue = Venue("Canada Place", address)
event = Event(time(9,0), time(2,30), venue)

print(event.venue.address.zipcode)
print(event.venue.address.country)
print(event.venue.address.street)
print(event.venue.name)
print(event.startTime)
print(event.endTime)
