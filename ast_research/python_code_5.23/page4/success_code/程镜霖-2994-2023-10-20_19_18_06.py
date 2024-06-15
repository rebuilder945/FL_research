y=input().split(",")
lst=list(y)
n,m=eval(input())
if abs(n)<len(lst):
    x=[lst[n] for i in range(m)]
    lst2=lst+x
    lst3=[]
    for i in lst2:
        lst3.append(int(i))
    print(lst3)
else:
    print("error")
