a=list(input().split(' '))
letter=input().split(' ')
x=int(letter[0])
y=int(letter[1])
b=[]
c=a[x]
b.append(c)
a[x]=a[y]
a[y]=b[0]
print(a)

