a=input().split(",")
b=input().split(",")
lst1=[]
for i in range(0,len(a)):
    lst=[]    
    lst.append(a[i])
    lst.append(int(b[i]))
    lst1.append(lst)
lst1.sort(key=lambda x:x[1])
print(lst1)
