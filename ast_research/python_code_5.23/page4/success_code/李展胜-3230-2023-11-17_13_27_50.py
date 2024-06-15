a=eval(input())
a.sort(reverse=True)
c=''.join(str(i) for i in a)
print(int(c))
