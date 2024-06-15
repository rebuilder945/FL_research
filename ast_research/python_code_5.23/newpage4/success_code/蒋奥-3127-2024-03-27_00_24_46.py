n=eval(input())
a=[ i+1 for i in range(n)]
b=a[0]
a.remove(b)
a.append(b)
print(a)
