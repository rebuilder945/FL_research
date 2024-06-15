a=input()
b=input()
lst=["red","blue","yellow"]
if a==b:
    print("error")
elif a in lst and b in lst:
    if a in lst[0:2] and b in lst[0:2]:
        print("purple")
    elif a in lst[0::2] and b in lst[0::2]:
        print("orange")
    else:
        print("green")
else:
    print("error")
