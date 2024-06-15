x = input().split(',')
y = eval (input())
x1 = list(x)
m = len(x1)
lst = []
for i in range(0,m):
    n = []
    n.append(x1[i])
    n.append(y[i])
    lst.append(n)
print(lst)    
