#Form a code with a specific format of using the letters of the value assigned to the variable


#basic split() program with manual selection of letters

student_id = input("Enter the student id:")
student_fn = input("Enter the first name of the student:")
student_ln = input("Enter the last name of the student:")
message = "I am a newbie In Whitecliffe college !"

#selecting the letters manually with the help of index
s1=(student_id[0])
s2=(student_id[1])
length= len(student_ln)
s3=(student_ln[length-3])
s4=(student_ln[length-2])
s5=(student_ln[length-1])

words = message.split()          #using in-built split () function
print("words=", words)
for i in words:
    if i == "Whitecliffe" or i == "college":
        print(i)
print("studentcode=", s1+s2+s3+s4+s5)  #display the output of the string operations
