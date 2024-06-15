n=eval(input())
m=1
z=2
h=0
for x in range(1,n+1):
    m+=x-1
    z+=x-1
    h+=z/m
print('%.4f'%h)

