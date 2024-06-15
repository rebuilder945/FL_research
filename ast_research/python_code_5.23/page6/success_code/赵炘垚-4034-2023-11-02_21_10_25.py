n=input()
m=input()
if n=="red":
    if m=="red":
        print("error")
    if m=="blue":
        print("purple")
    if m=="yellow":
        print("orange")
elif n=="yellow":
    if m=="red":
        print("orgenge")
    if m=="blue":
        print("green")
    if m=="yellow":
        print("error")
elif n=="blue":
    if m=="red":
        print("purple")
    if m=="blue":
        print("error")
    if m=="yellow":
        print("green")
else:
    print("error")
