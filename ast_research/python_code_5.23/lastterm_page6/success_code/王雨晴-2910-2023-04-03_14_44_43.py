a=int(input())
b=int(input())
c=a
for x in range(b-1):
    c+=a*(0.5)**(x)
print('%.2f'%(c))

