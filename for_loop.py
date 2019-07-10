for i in range(1,11):
    print(i)

print("\n Next one")

for j in [1,2,3]:
    print(j)

print("\n Next one")

for j in [0,2,4,6,8,10,12,14,16,18]:
        print(j)

print("\n Next one")

def star():
    a = 1
    while a <5:
        print("****")
        a += 1

star()


def star():
    for i in range(0, 3):
            for j in range(0, i+1):
                print("*", end= "")
            print()
    for i in reversed(range(0,4)):
        for j in range(0,i+1):
            print("*",end="")
        print()


star()

print("NOTE")
[x * 10 if x % 2 == 0 else 0 for x in reversed(range(0, 9))]
