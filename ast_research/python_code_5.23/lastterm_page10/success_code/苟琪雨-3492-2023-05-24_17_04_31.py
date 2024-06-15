str=input()
lst=[]
for i in str:
    if str.count(i)==1:
        lst.append(i)
print(lst[0])
