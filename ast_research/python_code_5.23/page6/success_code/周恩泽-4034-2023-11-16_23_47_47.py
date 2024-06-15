n1=input()
n2=input()
if (n1=="blue" and n2=="red") or (n1=="red" and n2=="blue"):
    print("purple")
elif (n1=="yellow" and n2=="red") or (n1=="red" and n2=="yellow"):
    print("orange")
elif (n1=="blue" and n2=="yellow") or (n1=="yellow" and n2=="blue"):
    print("green")
else:
    print("error")

