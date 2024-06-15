primarycolor=['red','blue','yellow']
purple1=['red','blue']
orange1=['red','yellow']
green1=['blue','yellow']
a=input()
b=input()
if a in primarycolor and b in primarycolor:
    if a in purple1 and b in purple1:
        print("purple")
    elif a in orange1 and b in orange1:
        print("orange")
    elif a in green1 and b in green1:
        print("green")
else:
    print("error")
