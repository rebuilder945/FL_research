list=eval(input())
list.sort()
list.reverse()
a=[str(x) for x in list]
b=int(''.join(a))
print(b)
