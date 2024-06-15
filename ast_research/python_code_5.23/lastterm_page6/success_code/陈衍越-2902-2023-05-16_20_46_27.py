nm=2
nd=1
n=int(input())
sum=0
for i in range(n):
    sum=sum+nm/nd
    nm,nd=nd,nm
    nm=nm+nd
print('%.4f'%sum)

