a = input()
b = input()
lst = ['red','blue','yellow']
if a not in lst or b not in lst or a==b:
    print("error")
elif {a,b}=={'red','blue'}:
    print("purple")
elif {a,b}=={'red','yellow'}:
    print("orange")
else:
    print("green")


