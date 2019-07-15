def is_odd():
    numbers = [1,56,234,87,4,76,24,69,90,135]
    isOdd = []
    for a in numbers:
        if not(a %2 == 0):
            isOdd.append(a)
    
    print(isOdd)

is_odd()