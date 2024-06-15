a=input().split(",")
b=eval(input())
ls=[]
for i in range(len(a)):
    ls.append([a[i],b[i]])
ls.sort(key=lambda x:x[1])
print(ls)

