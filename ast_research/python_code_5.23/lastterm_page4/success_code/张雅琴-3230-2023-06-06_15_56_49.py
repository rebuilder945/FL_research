a=eval(input())
a.sort(reverse=True)
b=[a[i]*(10**(len(a)-1-i)) for i in range(0,len(a))]
print(sum(b))
