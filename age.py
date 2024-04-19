#Simple program to get the age by the birth year

dob=int(input("Enter your birth of year"))
current_year= 2024
age= current_year-dob
print(age)


#Another program to use date, month and year of birthday

# importing the module
from datetime import date

#defining the function
def calculateAge(birthDate):
    today = date.today()       #Fetch today's date from datetime
    age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
    return age

# Print age
print(calculateAge(date(1992, 1, 11)), "years")

