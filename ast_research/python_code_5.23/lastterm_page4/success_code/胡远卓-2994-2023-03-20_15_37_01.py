lst=list(eval(input()))
n,m=eval(input())
L=len(lst)
if n>=-L and n<L:
    x=lst[n]
    for i in range(m):
        lst.append(x)
    print(lst)
else:
    print("error")

