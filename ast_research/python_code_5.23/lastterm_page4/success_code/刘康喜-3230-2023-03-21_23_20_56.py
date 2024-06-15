a=eval(input())
a.sort()
a.reverse()
for i in range(0,len(a)-1):
    print(a[i],end='')
print(a[len(a)-1])


