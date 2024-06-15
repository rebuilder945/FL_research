l = eval(input())
n, m = eval(input()) #n, m = map(int,input().split(',')
ls1 = list(l)
ls = ls1.copy()
if n >= len(ls1)-1 or m >= len(ls1)-1:
    print("error")
else:
    ls[n] = ls1[m]
    ls[m] = ls1[n]
    print(ls)
        
