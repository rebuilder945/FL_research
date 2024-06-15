a=eval(input())
for i in a:
    x=0
    x+=i
y=x/len(a)
y=str(y);num=0
for i in range(len(y)):
    if y[i]!='.':
        num+=1
    else:
        break
z=y[num+1:]
if z=='0':
    print(y[:num])
else:
    print("%2.f"%float(y))


