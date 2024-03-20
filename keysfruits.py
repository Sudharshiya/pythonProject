def fruit_name(**kwargs):
    for i in kwargs.keys():
        print(i)

fruit_name(mangoes=1, oranges=2, apples=3)
