n=eval(input())
n.sort()
if n[-1]==0:
    print("0")
else:
    n.reverse()
    b=''.join(str(i) for i in n)
    print(b)
