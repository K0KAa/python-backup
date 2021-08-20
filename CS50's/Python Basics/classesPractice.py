class Flight():
    def __init__(self,capacity) :
        self.capacity =capacity
        self.passengers =[]
    
    def add_passenger(self,name):
        if not self.seats():
            return False
        else:
            self.passengers.append(name)
            return True
    
    def seats(self):
        return self.capacity-len(self.passengers)

flight = Flight(3)

people =["Kushal","Kattel","Kokaa","Fucker"]

for person in people:
    if flight.add_passenger(person):
        print("added")
    else:
        print("full")

print(flight.passengers)