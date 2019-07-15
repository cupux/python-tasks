from functools import reduce
words = ["Hello", "Word"]

def string(strings):
    return reduce(lambda x,y: x + ' ' + y,strings)

print(string(words))