lst=input().split(",")
n,m=eval(input())
long=len(lst)
if n>=long:
    print("error")
else:
    lst2=[int(i) for i in lst]
    num=lst2[n]
    newlist=[num]*m
    result=lst2+newlist
    print(result)
