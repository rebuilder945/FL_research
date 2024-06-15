n=list(input().split(','))
m=list(map(int,input().split(',')))
a=[[n[i],m[i]] for i in range(len(n))]
a.sort(key=lambda x: x[1])
print(a)

