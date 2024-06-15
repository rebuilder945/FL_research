n=eval(input())
sum=0
l=1
r=2
for i in range(n):
   sum+=r/l
   r,l=r+l,r
print('%.4f'%sum)
