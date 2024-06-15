a=input()
b=input()
color={"red":1,"blue":2,"yellow":3}
sums=color.get(a,10)+color.get(b,10)
if sums==3:
    print("purple")
elif sums==4:
    print("orange")
elif sums==5:
    print("green")
else:
    print("error")
