a=eval(input())
a.sort()
a.reverse()
b=''
for i in range(len(a)):
    b=b+str(a[i])
print(int(b))
