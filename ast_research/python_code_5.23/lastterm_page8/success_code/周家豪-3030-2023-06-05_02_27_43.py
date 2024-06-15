lst1=input().split(',')
lst2=input().split(',')
lst=[]
for i in range(len(lst1)):
    lst.append([lst1[i],eval(lst2[i])])
print(lst)
