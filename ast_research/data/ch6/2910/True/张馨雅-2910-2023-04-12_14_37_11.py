h=eval(input())
N=eval(input())
f=[h,]
for i in range(1,N):
    m=(h/(2**i))*2
    f.append(m)
print('%.2f'%(sum(f)))

