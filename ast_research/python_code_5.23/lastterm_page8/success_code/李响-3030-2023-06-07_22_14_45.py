m = input().split(',')
n = input().split(',')
x = list(map(int,n))
a = []
for i in range(len(m)):
    a.append([m[i],x[i]])
print(sorted(a,key = lambda x:x[1]))
