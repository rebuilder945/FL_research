a=eval(input())
a.sort(reverse=True) 
if a[0]!=0:
    a=''.join(map(str,a))
    print(a)
else:
    print(0)
