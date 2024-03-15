message=str(input("Enter your message:"))
count=0
for letters in message:
    if letters == "a" or letters == "e" or letters == "i" or letters == "o" or letters == "u":
        count += 1
print("The number of vowels in message:", count)
