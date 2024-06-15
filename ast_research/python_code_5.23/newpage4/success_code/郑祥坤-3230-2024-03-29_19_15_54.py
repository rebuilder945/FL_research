a=eval(input())
a.sort(reverse=True)
b="".join(str(x) for x in a)
print(int(b))
