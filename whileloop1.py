#A simple program to do grading using loop

score= float(input("Enter the score"))
while score>100 or score<0:
    score = float(input("Invalid score,Enter the valid score:"))


if score>=80:
    print("firstclass")

elif score>=60 and score<80:
    print("secondclass")

elif score>=50 and score<60:
    print("Pass")

elif score<50 and score>0:
    print("Fail")
