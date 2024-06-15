lst = eval(input()) # n <= m
n, m = map(int,input().split(","))
ls = lst[:]
if n >= len(lst) or m >= len(lst):
    print("error")
else:
    p = m - n
    while p > 0:
        del ls[int(n)] 
        p = p - 1  
    print(ls)            


        
