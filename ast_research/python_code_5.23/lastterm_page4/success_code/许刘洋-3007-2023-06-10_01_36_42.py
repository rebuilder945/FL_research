a=eval(input())
n,m=eval(input())
if m>(len(a)-1):
    print('error')
for i in range(n,m):
    a.pop(i)
print(a)
