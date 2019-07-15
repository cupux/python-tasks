numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

#a=[even.append(x) if x %2==0 for x in numbers]
b = [even for even in numbers if even > 0]
print(b)



numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]

#a=[even.append(x) if x %2==0 for x in numbers]
b = [even for even in numbers if even % 2 == 0]
print(b)

words = ["hello", "my", "name", "is", "Sam"]

#a=[even.append(x) if x %2==0 for x in numbers]
b = [(word, len(word)) for word in words]
#print(len(b).upper())
print(b)

