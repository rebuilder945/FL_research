lst=eval(input())
n,m=map(int,input().split(','))
if n>=0 or m<=len(lst)+1:
    del(lst[n:m])
    print(lst)
else :
    print("error")
