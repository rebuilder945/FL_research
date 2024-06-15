import math
def mowei(l,m,n):
    if m != math.floor(m):
        print("error")
    else:
        if m >= (-len(l)) and n < len(l):
            x = l[m]
            for i in range(n):
                l.append(x)
            print(l)
        else:
            print("error")
nums = list(eval(input()))
m,n = eval(input())
mowei(nums,m,n)

