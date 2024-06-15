a=eval(input())
a=str(a)
a=list(a)
b=[]
for i in a:
    i=(int(i)+5)%10
    b.append(i)
b.reverse()
print(''.join(str(i) for i in b))

