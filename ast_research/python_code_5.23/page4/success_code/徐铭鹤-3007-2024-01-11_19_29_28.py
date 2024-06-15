a=input()
b,c=input().split(',')
if int(b)>len(a) or int(c)>len(a):
    print('error')
d=a[:(int(b)-1)]+a[int(c):]
print(d)
