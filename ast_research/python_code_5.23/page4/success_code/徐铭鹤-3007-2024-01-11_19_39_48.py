a=input()
b,c=input().split(',')
c=a[:(int(b)-1)]+a[int(c):]
print(c)

