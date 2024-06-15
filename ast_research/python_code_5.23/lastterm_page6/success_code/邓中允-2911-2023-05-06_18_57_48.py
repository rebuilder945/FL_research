n=eval(input())
a=str(n)
for i in range(len(a)):
    a[i]=(a[i]+5)%10
a.reverse()
print(a)
