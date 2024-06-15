a=input().split(",")
b=input().split(",")
l=[]
for i in range(len(a)):
    l.append([a[i],int(b[i])])
l.sort(key=lambda x:x[1])
print(l)

    

