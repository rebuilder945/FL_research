n = int(input())
l = [i for i in range(1,n+1)]
a = list[0]
for i in range(0,len(l)-1):
    l[i] = l[i+1]
l[-1] = a
print(l)
