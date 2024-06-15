a = list(map(int,input().split(",")))
m ,n=eval( input())
if m<len(a):
   b =  [a[m]]*n
   d = a+b
   print(d)


else:
   print('error')


