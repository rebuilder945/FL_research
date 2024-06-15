num=eval(input())
n,m=eval(input())
le=len(num)
if n<m and m<=le-1:
    l=m-n
    for i in range(l):
        del num[n]
        n+=1
    print(num)
elif n==m and m<=le-1:
    print(num)
else:
    print('error')      
