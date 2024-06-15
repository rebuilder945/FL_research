n=eval(input())
sum=2
l=1
r=2
for i in range(n-1):
   sum+=(l+r)/l
   r,l=r+l,r
print('%.4f'%sum)
