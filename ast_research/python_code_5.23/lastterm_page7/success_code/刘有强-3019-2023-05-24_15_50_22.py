
a,b,c,d=input().split()
e=(int(b)+int(c)+int(d))/3
if int(b) > int(c) > int(d):
    print(a,'%.2f'%int(b),'%.2f'%int(c),'%.2f'%int(d),'%.2f'%e)
elif int(b) > int(d) > int(c):
    print(a,'%.2f'%int(b),'%.2f'%int(d),'%.2f'%int(c),'%.2f'%e)
elif int(c) > int(b) > int(d):
    print(a,'%.2f'%int(c),'%.2f'%int(b),'%.2f'%int(d),'%.2f'%e)
elif int(c) > int(d) > int(b):
    print(a,'%.2f'%int(c),'%.2f'%int(d),'%.2f'%int(b),'%.2f'%e)
elif int(d) > int(b) > int(c):
    print(a,'%.2f'%int(d),'%.2f'%int(b),'%.2f'%int(c),'%.2f'%e)
elif int(d) > int(c) > int(b):
    print(a,'%.2f'%int(d),'%.2f'%int(c),'%.2f'%int(b),'%.2f'%e)
else:
    print(a,'%.2f'%int(d),'%.2f'%int(c),'%.2f'%int(b),'%.2f'%e)
