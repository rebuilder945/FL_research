a=eval(input())
a.sort(reverse=True)
b="".join(map(str,a))
if max(a)==0:
    print(0)
print(b)
