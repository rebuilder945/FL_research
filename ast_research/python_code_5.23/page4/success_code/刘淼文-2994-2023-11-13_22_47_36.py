lst = map(input().split())
n,m = eval(input())
lst2 = []
if n >= len(lst):
    print("error")
else:
    lst2 =[lst[n]]*m
    l = lst + lst2
    print(l)
    
