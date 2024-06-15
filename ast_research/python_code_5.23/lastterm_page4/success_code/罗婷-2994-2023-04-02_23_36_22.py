lst=eval(input())
n,m=eval(input())
lst1=list(lst)
lst2=[]
if n>=len(lst):
    print("error")
else:
    lst2.append(lst[n])
    lst2=lst2*m
    lst1=lst+lst2
    print(lst1)
