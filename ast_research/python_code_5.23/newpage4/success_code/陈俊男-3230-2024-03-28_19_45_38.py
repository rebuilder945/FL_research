a=eval(input())
a.sort(reverse=True)
b="".join(str(i) for i in a)
print(int(b))
