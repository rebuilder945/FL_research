y=input().split(",")
lst=list(y)
n,m=eval(input())
if abs(n)<len(lst):
    x=[lst[n] for i in range(m)]
    lst2=lst+x
    print(lst2)
else:
    print("error")
