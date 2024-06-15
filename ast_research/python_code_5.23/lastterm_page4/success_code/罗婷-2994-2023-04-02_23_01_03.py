lst=eval(input())
n,m=eval(input())
lst1=list(lst)
lst2=[]
if n>=len(lst):
    print("error")
else:
    lst2=lst[n]
    lst2=lst2*m
    lst1.append(lst2)
    print(lst1)
