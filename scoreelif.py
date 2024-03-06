score= float(input("Enter the score"))
if score>=0 and score<=100:

    if score>=80:
        print("firstclass")

    elif score>=60 and score<80:
        print("secondclass")

    elif score>=50 and score<60:
        print("Pass")

    elif score<50 and score>0:
        print("Fail")

else:
    print("Invalid score")