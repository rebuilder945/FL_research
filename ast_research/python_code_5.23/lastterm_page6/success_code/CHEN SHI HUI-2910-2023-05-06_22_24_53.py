h=int(input())
N=int(input())
l=[h]
for i in range(1,N):
    a=(h*0.5**i)*2
    l.append(a)
print('%.2f'%sum(l))
