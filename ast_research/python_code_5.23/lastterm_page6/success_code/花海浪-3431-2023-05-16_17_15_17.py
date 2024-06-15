color=["red","blue","yellow"]
a=input()
b=input()
if a not in color or a==b or b not in color:
    print("error")
else:
    c=[]
    c.append(a)
    c.append(b)
    if "red" not in c:
        print("green")
    elif "blue" not in c:
        print("orange")
    else:
        print("purple")

    
    
