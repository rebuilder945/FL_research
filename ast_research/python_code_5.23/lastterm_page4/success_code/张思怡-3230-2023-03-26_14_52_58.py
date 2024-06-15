a=eval(input())
a.sort(reverse=True)
b=[a[i]*10**(len(a)-i-1) for i in range(len(a))]

print(sum(b))
