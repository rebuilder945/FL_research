ls = list(eval(input()))
n,m = eval(input())
lscopy = ls.copy()
if len(ls)+n<=0 or n>=len(ls):
    print("error")
else:
    for i in range(m):
        ls.append(lscopy[n])
    print(ls)
