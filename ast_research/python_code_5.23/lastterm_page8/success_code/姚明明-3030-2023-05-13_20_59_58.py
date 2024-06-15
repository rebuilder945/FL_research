a=input().split(",")
b=input().split(",")
lst=[]
for i in range(len(a)):
    lst.append([a[i],b[i]])
lst.sort(reverse=False)
print(lst)
