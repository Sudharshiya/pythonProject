class Arithmetic:
    #initialise the attributes
    def __init__(self, firstnum, secondnum):
        self.firstnum= firstnum
        self.secondnum= secondnum


    def addition(self):
        sum= self.firstnum + self.secondnum
        return (sum)

    def subtraction(self):
        sub= self.firstnum - self.secondnum
        return (sub)

    def multiplication(self):
        mul= self.firstnum * self.secondnum
        return mul

cal= Arithmetic(9,3)
print(cal.addition())
print(cal.subtraction())
print(cal.multiplication())
