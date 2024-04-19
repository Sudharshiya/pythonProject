#a simple program to calculate area of the triangle

# Assigning a value to the variables a,b,c
a = 7
b = 8
c = 9

#calculate the value of s in the Area formula
s = (a+b+c)/2

#Calculate the area of the triangle
Area=(s*(s-a)*(s-b)*(s-c))**0.5
print(Area) # Display the result of the area
