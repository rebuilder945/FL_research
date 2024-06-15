n=eval(input())
c=0
if n <=100:
    print("none")
elif n>100 and n<=999:
    for x in range(100,n+1,1):
        b=str(x)
        if int(b[0])**3+int(b[1])**3+int(b[2])**3==int(b):
            print(b)
            c+=1
    if c==0:
        print("none")
elif n>999:
    for x in range(100,1000,1):
        b=str(x)
        if int(b[0])**3+int(b[1])**3+int(b[2])**3==int(b):
            print(b)
