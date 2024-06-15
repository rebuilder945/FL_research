a=str(input())
b=[]
c=''
for i in a:
    i=(int(i)+5)%10
    b.append(i)
b.reverse()
for i in b:
    c=c+str(i)
print(c)
