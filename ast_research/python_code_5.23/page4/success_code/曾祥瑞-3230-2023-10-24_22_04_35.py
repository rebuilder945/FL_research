a=eval(input())
a.sort(reverse=True)
if max(a)==0:
    print("0")
else:
    a=[str(i) for i in a]
    b=''.join(a)
    print(b)
