even = int(input("Enter a number: "))

def is_even(a):
    if a%2 == 0:
        return True
    else:
        return False
    numbers = [1,56,234,87,4,76,24,69,90,135]
    isEven = []
    for a in numbers:
        if a %2 == 0:
            isEven.append(a)
            
print(is_even(even))

print("\t\tlist")