lst=list(input())
n,m=eval(input())
if n>=len(lst):
    print("error")
else:
    lst1=[lst[n]*m]
    print(lst+lst1)
