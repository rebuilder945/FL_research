a=input()
b=0
c=[]
if int(a)>=135:
    for i in range(101,int(a)+1):
        c.append(i)
    for i in c:
        d=str(i)
        for j in d:
            b+=int(j)**3
        if b==int(d):
            print(i)
elif int(a)<135:
    print('none')

