n,m=input().split(" ")
n=eval(n)
m=eval(m)
if m-n<3 or m<0 or n<0 or m>=10:
    print('illegal input')
else:
    date=[]
    date1=[]
    for i in range(n,m):
        date.append(i)
    for i in date:
        for j in date:
            for x in date:
                g=i*100+j*10+x
                date1.append(g)
for x in date1:
    if x>99:
        x=str(x)
        if x[0]!=x[1] and x[1]!=x[2] and x[0]!=x[2]:
            print(x,end=' ')
