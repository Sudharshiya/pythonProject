student_id = input("Enter the student id:")
student_fn = input("Enter the first name of the student:")
student_ln = input("Enter the last name of the student:")
message = "I am a newbie In Whitecliffe college !"
words = message.split()
print("words=", words)
s1= student_id[:2]
s2= student_ln[:3]
for i in words:
    if i == "Whitecliffe":
        if i == "college":
            print(s1,s2)
