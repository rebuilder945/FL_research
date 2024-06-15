lst=eval(input())
n,m=eval(input())
lst=list(lst)
lst2=[]
if n>=len(lst) or n<(-len(lst)):
    print("error")
else:
    lst2.append(lst[n])
    lst2=lst2*m
    lst=lst+lst2
    print(lst)
