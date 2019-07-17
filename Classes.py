from functools import reduce
word =["Micheal", "Bright", "Joseph"]
def jkm(m):
    return reduce(lambda a ,y: a + ')' + y ,m)
print(jkm(word))