n=input()
m=input()
a=["red","blue","yellow"]
if n in a and m in a and n!=m:
    if n=="red" and m=="blue":
        print("purple")
    if n=="red" and m=="yellow":
        print("orange")
    if n=="blue" and m=="red":
        print("purple")
    if n=="yellow" and m=="red":
        print("orange")
    if n=="yellow" and m=="blue":
        print("green")
    if n=="blue" and m=="yellow":
        print("green")
else:
    print("error")

