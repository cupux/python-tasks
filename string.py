def noVowel(s):
    'return True if string s contains no vowel, False otherwise'
    for char in s:
        if char.lower() in 'a':
            return True
    return False
    
print(noVowel(input("Enter:  ")))

print("This is for two letters\n")
def noVowel(s):
    'return True if string s contains no vowel, False otherwise'
    for char in s:
        if char.lower() in ('s' and 'k'):
            return True
    return False

def jkm():
    jkm.function(noVowel)
    print(noVowel(input("Enter:  ")))

jkm()