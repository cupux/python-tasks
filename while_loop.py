i = 6
while(i < 19):
    i = i + 1
    print (i)

print("Even numbers")
i = 12
while(i < 20):
    i = i + 2
    print (i)

print("All even numbers")
def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

for i in reversed(range(0,20)):
	print(i)


def Reverse_Integer(Number):
    Reverse = 0
    while(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Number = Number //10
    return Reverse

Number = int(input("Please Enter any Number: "))
Reverse = Reverse_Integer(Number)
print("\n Reverse of entered number is = %d" %Reverse)

a= ["Jow","uui"]
a.insert(6,"jkm")
print(a)
