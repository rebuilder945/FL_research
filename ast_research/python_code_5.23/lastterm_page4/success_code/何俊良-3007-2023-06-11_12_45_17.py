lst=eval(input())
n,m=map(int,input())
if n>m and m>len(lst) and n<=0:
    print('error')
else:
    del lst[n,m-1]
    print(lst)
