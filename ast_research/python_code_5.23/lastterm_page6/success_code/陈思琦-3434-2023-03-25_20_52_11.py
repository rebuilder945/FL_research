a=(input())
b=(input())
if a in ['red']:
    if b in ['red']:
        print("error")
    if b in ['blue']:
        print("purple")
    if b in ['yellow']:
        print("orange")
elif a in ['blue']:
    if b in ['red']:
        print("purple")
    if b in ['blue']:
        print("error")
    if b in ['yellow']:
        print("green")
elif a in ['yellow']:
    if b in ['red']:
        print("orange")
    if b in ['blue']:
        print("green")
    if b in ['yellow']:
        print("error")
else:
    print("error")

