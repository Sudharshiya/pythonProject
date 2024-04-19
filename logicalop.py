#A simple program to learn the logical operators like and, or, not...etc

#assigning the values to x and y variable
x = 4
y = 1

# assigning the output of the logical operations with a variable
a = x & y    #and operator
b = x | y    #or operator
c = ~x       # not operator
d = x ^ 5    # bitwise xor
e = x >> 2    # bitwise right shift operator
f = x << 2     #bitwise left shift operator

print(a, b, c, d, e, f)
