a=eval(input())
a.sort(reverse=True)
if a.count(0)==len(a):
    print(0)
else:
    b=''.join(str(x)for x in a)
    print(b)
