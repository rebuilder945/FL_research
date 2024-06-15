m=input().split(",")
n=eval(input())
ls=[]
for i in range(len(m)):
    ls.append([m[i],n[i]])
d=dict(ls)
d.sort(reverse=False)
print(list(d))
