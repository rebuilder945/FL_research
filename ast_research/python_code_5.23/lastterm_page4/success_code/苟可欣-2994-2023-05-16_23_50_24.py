ls=eval(input())
n,m=eval(input())
if n>len(ls)-1:
    print("error")
else:
    for x in range(m):
        ls.append(ls[n])
    print(ls)
