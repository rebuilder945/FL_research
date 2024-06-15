lst=eval(input())
n,m=map(int,input().split(','))
if n>0 or m<=len(lst):
    del(lst[n:m])
    print(lst)
else :
    print("error")
