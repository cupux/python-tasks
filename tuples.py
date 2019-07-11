def partition():
    a = int(input("Input a number: "))
    if a % 2 ==0:
        print("(",a,", none )")
    else:
        print("(none,",a,")")
        
partition()

def jkm():
    b = []
    v = []
    s = int(input("Input a number: "))
    a = int(input("Input a number: "))
    for q in range(s, a):
    
        if q % 2 ==0:
            b.append(q)
            
        else:
            v.append(q)
        
        
    print(b)
    print(v)
jkm()