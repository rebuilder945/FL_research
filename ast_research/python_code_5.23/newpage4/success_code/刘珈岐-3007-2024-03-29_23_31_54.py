lst=eval(input())
n,m=input().split(',')
n=int(n)
m=int(m)
lst1=[]
if int(n)<len(lst) and int(m)<len(lst):
    if n<m:
        del lst[n:m]
        print(lst)
    else:
        del lst[m+1:n+1]
        print(lst)
else:
    print('error')        
