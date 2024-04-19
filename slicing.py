#Slicing program and using split function

student_id = input("Enter the student id:")
student_fn = input("Enter the first name of the student:")
student_ln = input("Enter the last name of the student:")
message = "I am a newbie In Whitecliffe college !"
words = message.split()
print("words=", words)
s1= student_id[:2]  #slicing the first two indexes
s2= student_ln[:3]  #slicing the first three indexes
for i in words:
    if i == "Whitecliffe":        #check these strings are in 'words' 
        if i == "college":
            print(s1,s2)
