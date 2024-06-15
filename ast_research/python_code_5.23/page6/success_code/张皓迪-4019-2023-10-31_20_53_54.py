from random import randint


a=str(input())
b=[]
for i in a:
    c=(int(i)+5)%10
    b.append(c)
b.reverse()
m=''
for i in b:
    m+=str(i)
print(m)

