from re import L


l = eval(input())
n,m = eval(input())
if n >= len(l) or m >= len(l):
    print("eroor")
else:
    if n <= m:
        del l[n:m]
    else:
        del l[n:m:-1]
    print(l)
        

