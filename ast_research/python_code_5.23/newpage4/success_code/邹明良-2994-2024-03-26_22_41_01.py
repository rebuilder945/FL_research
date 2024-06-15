ls = list(eval(input()))
n,m = eval(input())
if len(ls)+n<=0 or n>=len(ls):
    print("error")
else:
    for i in range(m):
        ls.append(ls[n])
    print(ls)
