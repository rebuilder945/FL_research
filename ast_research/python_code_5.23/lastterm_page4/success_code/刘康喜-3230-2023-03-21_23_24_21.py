a=eval(input())
a.sort()
a.reverse()
if max(a)==0:
    b=1
else:
    for i in range(0,len(a)-1):
        print(a[i],end='')
print(a[len(a)-1])


