a=eval(input())
n,m=input().split(',')
if int(n)>len(a)-1 or int(m)>len(a)-1:
    print('error')
else:
    del a[int(n),int(m)]
    print(a)
    
