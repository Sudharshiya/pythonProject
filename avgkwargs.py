# the single-asterisk form of *args can be used as a parameter, able to pass in as many arguments as we wished into the function calls.
# The double asterisk form of **kwargs is used to pass a keyworded, variable-length argument dictionary to a function.


#defining the function with keyworded arguments as a parameter
def average_stu(**kwargs):
    sum=0

    for i in kwargs.values():        #for-loop to get the keyvalue for number of arguments(4)
        sum= sum+i
        avg= sum/len(kwargs)         #here, it finds the length of the keyword(4)
    return sum, avg

k = average_stu(IT5014=60, IT7809=80, IT6798=50, IT5048=70)  #object k to call the function
print("Sum & average=", k)      #display k, the output
