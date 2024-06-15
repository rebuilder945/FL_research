s={"red":1,"blue":2,"yellow":3}
n1=input()
n2=input()
s=s.get(n1,10)+s.get(n2,10)
if s==3:
    print('purple')
elif s==4:
    print('orange')
elif s==5:
    print('green')
else:
    print('error')
