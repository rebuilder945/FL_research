a=eval(input())
x,y=map(int,input().split(','))
c=len(a)
if x>y or y>c:
     print('error')
else:
    del a[x:y]
    print(a)

