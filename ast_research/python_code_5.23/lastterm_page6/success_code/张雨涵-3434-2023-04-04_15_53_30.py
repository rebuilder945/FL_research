a = input()
b = input()
c = [a,b]
d = set(c)
pcolor = {"red","yellow","blue"}
if d.issubset(pcolor):
    if d == {"red","blue"}:
        print("purple")
    elif d =={"red","yellow"}:
        print("orange")
    elif d == {"yellow","blue"}:
        print("green")
    else:
        print("error")
else:
    print("error")
