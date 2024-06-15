lst = eval(input()) # n <= m
n, m = eval(input())
ls = lst
if n >= len(lst)-1 or m >= len(lst)-1:
    print("error")
else:
    p = m - n
    while p > 0:
        del ls[int(n)] 
        p = p - 1  
    print(ls)            


        
