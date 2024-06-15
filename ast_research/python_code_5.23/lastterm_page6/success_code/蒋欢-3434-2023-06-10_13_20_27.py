c1=input().lower()
c2=input().lower()
primaryColor=["red","blue","yellow"]
colors=set([c1,c2])
if c1==c2 or (c1 not in primaryColor) or (c2 not in primaryColor):
    print("error")
else:
    if colors=={"red","blue"}:
        print("purple")
    elif colors=={"red","yellow"}:
        print("orange")
    else:
        print("green")
