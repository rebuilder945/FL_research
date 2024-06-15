a=str(input())
b=[]
for i in a:
    i=(int(i)+5)%10
    b.append(i)
b.reverse()
for k in range(len(b)):
    print(b[k],end='')


