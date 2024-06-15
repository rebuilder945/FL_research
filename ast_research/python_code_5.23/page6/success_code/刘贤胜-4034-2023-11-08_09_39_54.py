a=input()
b=input()
if a not in {"red","blue","yellow"} and b not in {"red","blue","yellow"} and  a==b :
    c={a,b}
    if c=={"red","blue"}:
        print("purple")
    elif c=={"red","yellow"}:
        print("orange")
    elif c=={"blue","yellow"}:
        print("green")
else:
     print("error")

