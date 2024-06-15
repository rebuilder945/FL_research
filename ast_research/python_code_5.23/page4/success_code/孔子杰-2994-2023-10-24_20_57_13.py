lst=list(eval(input()))
n,m=eval(input())
if n>len(lst) and n>0:
    print("error")
else:
    str=lst[n]*m
    lst1=list(str)
    lst2=lst+lst1
    print(lst2)
