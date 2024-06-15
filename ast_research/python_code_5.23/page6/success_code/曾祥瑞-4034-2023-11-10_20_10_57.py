n=eval(input())
m=eval(input())
a={"red":1,"blue":2,"yellow":3}
if n==m or n not in a or m not in a:
    print("error")
else:
    b=a.get(n)+a.get(m)
    if b==3:
        print("purple")
    if b==4:
        print("orange")
    if b==5:
        print('green')
