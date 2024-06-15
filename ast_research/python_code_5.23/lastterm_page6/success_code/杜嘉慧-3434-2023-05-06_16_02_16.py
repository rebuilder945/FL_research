a=input()
b=input()
s={"red":1,"blue":2,"yellow":3}
sum=s.get(a)+s.get(b)
if sum==3:
    print("purple")
elif sum==4:
    print("orange")
elif sum==5:
    print("green")
else:
    print("error")

