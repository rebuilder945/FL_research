a=input()
b=input()
c={a,b}
if c=={"red","blue"}:
    print("purple")
elif c=={"red","yellow"}:
    print("orange")
elif c=={"blue","yellow"}:
    print("green")
else :
    if a not in {"red","blue","yellow"} and b not in {"red","blue","yellow"} or a==b:
        print("error")


