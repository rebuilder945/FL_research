n,m,l=eval(input())
list=[]
x=n
list.append(x)
for i in range(m-1):
    x=x+l
    list.append(x)
print(list)
