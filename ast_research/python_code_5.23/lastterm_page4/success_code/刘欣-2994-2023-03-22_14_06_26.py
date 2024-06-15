ls=list(eval(input()))
n,m=eval(input())
for i in range(m):
    if n < len(ls) and n > -len(ls):
        ls.pop(n-1)
        ls.append(ls.pop(n-1))
        print(ls)
    else:
        print("error")
