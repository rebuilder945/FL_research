a=eval(input())
a.sort(reverse=True)
b=0
for i in range(0,len(a)):
    b=a[i]*10**(len(a)-i-1)+b
print(b)


