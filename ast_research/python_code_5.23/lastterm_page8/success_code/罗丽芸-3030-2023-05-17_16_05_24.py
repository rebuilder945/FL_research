a=input().split(",")
b=eval(input())
f=[]
for i in range (len(b)):
    f.append([a[i],b[i]])
f.sort(key=lambda x:x[1])
print(f)
