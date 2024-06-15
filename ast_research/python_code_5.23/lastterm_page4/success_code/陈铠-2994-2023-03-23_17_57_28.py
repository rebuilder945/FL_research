lst=list(eval((input())))
n,m=eval(input())
if n>=0 and n<len(lst):
    num=[lst[n]]*m
    lst.extend(num)
    print(lst)
    if n<0 and n>=-len(lst):
        num=[lst[n]]*m
    lst.extend(num)
    print(lst)
else:
    print("error")
