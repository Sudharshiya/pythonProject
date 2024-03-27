class Cars:
    #initialise the function
    def __init__(self, name, speed, mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage
    #end of the Initialisation

    def brand(self):
        return(" The name of the car is " + self.name)

    def mil(self):
        kmhr= self.mileage*10
        return (kmhr)

n= Cars("VolvoXC90", "180km/hr", 11.04)

print(n.brand())
print(n.mil())

