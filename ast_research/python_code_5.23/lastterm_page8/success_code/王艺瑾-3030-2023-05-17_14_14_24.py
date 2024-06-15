a=input().split(",")
b=input().split(',')

d=[]
for x in range(len(a)):
    d.append([a[x],int(b[x])])
d.sort(key=lambda x:x[1])
print(d)

            


