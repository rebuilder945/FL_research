a=eval(input())
a.sort(reverse=True)
a=[str(i) for i in a]
if max(a) ==0:
    print("0")
else:
    b=''.join(a)
    print(b)
