#Check for the vowels in the message

message=str(input("Enter your message:"))
count=0
for letters in message:
    if letters == "a" or letters == "e" or letters == "i" or letters == "o" or letters == "u":        #vowels in lowercase will be found
        count += 1          #count the vowels one by one in the message and add it together
print("The number of vowels in message:", count)      #display the count of vowels in the message
