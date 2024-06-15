a=input()
b=input()
if a and b not in ("red","blue","yellow"):
    print("error")
elif a==b:
    print("error")
elif a in ("red","blue") and b in ("red","blue"):
    print("purple")
elif a in ("red","yellow") and b in ("red","yellow"):
    print("orange")
elif a in ("blue","yellow") and b in ("blue","yellow"):
    print("green")
else:
    print("error")
