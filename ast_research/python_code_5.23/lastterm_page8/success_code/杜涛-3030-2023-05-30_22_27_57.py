m=input().split(',')
n=list(map(eval,input().split(',')))
a=[]
for i in range(len(n)):
    a.append([m[i],n[i]])
a.sort(key=lambda x:x[1],reverse=False)
print(a)

