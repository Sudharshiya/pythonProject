# a dictionary can be created by placing a sequence of elements within curly {} braces, separated by a ‘comma’.

#a simple program to display the key with the value
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])   #print the dictionary content with an added symbol -> instead of :

