n=eval(input())
n.sort(reverse=True)
if sum(n)==0:
    print(0)
else:
    a=[str(x)for x in n]
    print("".join(a))

    





