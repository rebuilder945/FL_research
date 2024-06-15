c1 = eval(input())
c2 = eval(input())
if (c1=="red" and c2=="blue") or (c2=="red" and c1=="blue"):
    print("purple")
elif (c1=="red" and c2=="yellow") or (c2=="red" and c1=="yellow"):
    print("orange")
elif (c1=="yellow" and c2=="blue") or (c2=="yellow" and c1=="blue"):
    print("green")
else:
    print("error")
