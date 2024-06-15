n=eval(input())
n.sort(reverse=True)
ls=[str(x) for x in n]
a=''.join(ls)
print(int(a))
