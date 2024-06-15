a = eval(input())
b = eval(input())
c =['red','blue','yellow']
d = ['red','blue']
e = ['red','yellwo']
f = ['blue','yellow']
if a in c and b in c and a != b:
    if a in d and b in d:
        print("purple")
    elif a in e and b in e:
        print("orange")
    elif a in f and b in f:
        print("green")
elif a == b:
    print("error")
elif a not in c or b not in c:
    print("error")
