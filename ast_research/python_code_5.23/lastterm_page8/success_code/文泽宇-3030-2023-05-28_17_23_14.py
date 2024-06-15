n=input().split(',')
m=input().split(',')
m=[int(d) for d in m]
lst=[]
for i in range(0,len(n)):
    x=[n[i],m[i]]
    lst.append(x)
lst.sort(key=lambda x : x[1])
print(lst)
