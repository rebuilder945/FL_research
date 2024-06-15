lst=list(eval(input()))
n,m=eval(input())
if n <len(lst):
    lst2=list(lst(n))*m
    print(lst+lst2)
else:
    print("error")
