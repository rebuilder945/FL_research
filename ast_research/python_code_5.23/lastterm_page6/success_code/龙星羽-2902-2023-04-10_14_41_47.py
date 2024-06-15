list=[1,2]
s=[]
n=eval(input())
for i in range (n):
    z=list[i]+list[i+1]
    list.append(z)
for i in range(n):
    a=list[i+1]/list[i]
    s.append(a)
print('%.4f'%sum(s))
