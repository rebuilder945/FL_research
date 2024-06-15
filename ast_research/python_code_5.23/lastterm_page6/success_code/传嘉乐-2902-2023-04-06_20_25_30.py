n=int(input())
i=2
j=1
k=1
a=0
while n>0:
    a+=i/j
    j=i
    i=i+k
    k=j
    n-=1
print('%.4f'%a)


