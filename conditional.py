
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
    


print("\n\n\t\tthe year they were born")
print("\n")

def tell_age():
    age = int(input("Which year were you born: "))
    if age > 1919:
        ans = 2019 - age
        print("You are ",ans, "years old")
    else:
        print("You think you can be that old errrrr u r joking!!:(")
    
tell_age()

print("\n\n\t\tThe leap year cal.")
print("\n")

def leap_year():
    year = int(input("Which year were you born: "))
    if (year % 400) == 0 or ((year % 100) == 0) or ((year % 4) == 0):
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))

leap_year()
    