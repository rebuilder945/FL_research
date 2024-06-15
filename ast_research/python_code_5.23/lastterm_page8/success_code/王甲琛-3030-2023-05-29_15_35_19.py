a=input().split(",")
b=list(map(int,input().split(",")))
lst=[]
for x in range(len(a)):
    lst.extend([[a[x],b[x]]])
lst.sort(key=lambda x: x[1])
print(lst)

