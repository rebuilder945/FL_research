a=eval(input())
if a.count(0)==len(a):
    print(0)
else:
    a.sort(reverse=True)
    b=str((i) for i in a)
    print(b)
