m = input().split(',')
n = input().split(',')
a = []
for i in range(len(n)):
    a.append([m[i],n[i]])
print(sorted(a,key = lambda x:x[1]))
