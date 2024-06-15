n=eval(input())
n.sort(reverse=True)
if max(n)==0:
    print("0")
else:
    m="".join(map(str,n))
    print(m)

