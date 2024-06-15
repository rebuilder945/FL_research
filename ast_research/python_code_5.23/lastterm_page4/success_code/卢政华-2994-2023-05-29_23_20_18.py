lst=list(eval(input()))
n,m=eval(input())
lst2=[]
if n <len(lst):
    lst3=list(lst(n))
    a=lst3*m
    lst2.append(a)
    print(lst+lst2)
else:
    print("error")
