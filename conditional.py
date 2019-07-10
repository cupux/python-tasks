
def even():
    a = [x * 10 if x % 2 == 0 else x for x in range(0, 20)]
    print(a)

even()



def age():
    a = int(input("How old are you: "))
    if a < 18:
        print("You are not old")
    else:
        print("You are old")

age()
    
