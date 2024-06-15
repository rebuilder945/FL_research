n=eval(input())
c=[]
if n>=999:
    for i in range(100,1000):
        b=str(i)
        if int(b[0])**3+int(b[1])**3+int(b[2])**3==i:
            c.append(i)
else:
    for i in range(100,n+1):
        b=str(i)
        if int(b[0])**3+int(b[1])**3+int(b[2])**3==i:
            c.append(i)
if c==[]:
    print('none')
else:
    for x in c:
        print(x)








