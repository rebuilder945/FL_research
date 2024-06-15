n,m,l=eval(input())
list=[n]
for i in range(m-1):
    x=n+(i+1)*l
    list.append(x)
print(list)

