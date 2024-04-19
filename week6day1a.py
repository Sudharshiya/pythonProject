#class with functions and methods

class Fruit:
    #initialise the parameters used in the class
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def func(self):
        print("Fruit is "+ self.name)

f1= Fruit("Apple", "Red")
print(f1.func())       #invocate the function
