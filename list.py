list = []
list.append(input("Input any string "))
            
print(list)



# f = [x if x % 2 == 0 else print(''.join(map(str,""))) for x in range(a, b)]
#f = [x if x % 2 == 0 else 0 for x in range(a, b)]
#print(f)


def get_evens(a,b):
    even_numbers = []
    print("the maximum number is ",max(a, b))
    print("The minimum number is ",min(a, b))
    for x in range(a,b):
        if x % 2 == 0:
            even_numbers.append(x)
    return even_numbers

print(get_evens(int(input("Enter a number: ")),int(input("Enter another number: "))))
print(get_evens(1, 10))
result = get_evens(15, 30)
print(result)
