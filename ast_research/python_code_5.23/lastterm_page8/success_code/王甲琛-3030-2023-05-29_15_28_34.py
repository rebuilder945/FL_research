a=input().split(",")
b=input().split(",")
lst=[]
for x in range(len(a)):
    lst.extend([[a[x],b[x]]])
print(lst)

