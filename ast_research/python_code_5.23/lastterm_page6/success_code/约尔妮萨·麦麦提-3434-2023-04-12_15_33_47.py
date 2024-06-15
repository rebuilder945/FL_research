s={"red":1,"blue":2,"yellow":3}
s1=input()
s2=input()
sum=s.get(s1,10)+s.get(s2,10)
if sum==3:
    print("purple")
elif sum==3:
    print("orange")
elif sum==5:
    print("green")
elif sum==1:
    print("red")
else:
    print("error")
