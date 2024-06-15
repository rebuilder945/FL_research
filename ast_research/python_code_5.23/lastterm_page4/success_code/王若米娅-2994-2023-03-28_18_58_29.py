str1=input().split(",")
n,m=eval(input())
lst=list(int(i)for i in str1)
if n>len(lst)-1:
    print("error")
else:
    a=lst[n]
    lst2=[a]*m
    lst3=lst+lst2
    print(lst3)
