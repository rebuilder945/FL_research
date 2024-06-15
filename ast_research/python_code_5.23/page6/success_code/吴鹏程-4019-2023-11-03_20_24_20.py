a=eval(input())
a=[]
for x in range(len(a)+1):
    a[x]=(a[x]+5)%10
for y in range(len(a)):
    y.append(int(a[y]))
a.reverse
print(a)
    


