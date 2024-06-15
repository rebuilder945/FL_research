lst=eval(input())
n,m=eval(input())
lst2=[]
if n <len(lst):
    a=lst[n]*m
    lst2.insert(0,a)
    print(lst+lst2)
else:
    print("error")
