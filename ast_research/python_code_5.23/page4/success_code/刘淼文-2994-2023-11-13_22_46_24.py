a = input().split()
lst = list(map(int,a))
n,m = eval(input())
lst2 = []
if n >= len(lst):
    print("error")
else:
    lst2 =[lst[n]]*m
    l = lst + lst2
    print(l)
    
