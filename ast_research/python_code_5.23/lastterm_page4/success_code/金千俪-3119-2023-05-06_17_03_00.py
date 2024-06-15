lst=eval(input())
lst1=[]
for i in lst[::-1]:
    if i not in lst1:
        lst1.append(i)
lst2=lst1.sort(reverse=True)
print(lst2)
