n,m,l=eval(input())
list=[n]
for i in range(m-1):
    n+=l
    list.append(n)
print(list)
