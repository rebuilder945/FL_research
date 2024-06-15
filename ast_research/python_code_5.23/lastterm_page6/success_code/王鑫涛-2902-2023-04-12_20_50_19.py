a = eval(input())
n=1
m=2
b=[]
for i in range(a):
    b.append(m/n)
    m+=n
    n=m-n
print('%.4f'%sum(b))
