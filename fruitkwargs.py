def fruit_price(**kwargs):
    sum=0
# add each values assigned to the key
    for i in kwargs.values():
        # adding the values
        sum = sum + i
        # return the value sum
    return sum


k = fruit_price(mango=10, Apple=5, Orange=15)
print("Sum of the fruits:", k)