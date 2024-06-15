lst=eval(input())
ma=max(lst)
mi=min(lst)
lst1=lst.copy()
for i in lst:
    if i==mi or i==ma:
        lst1.remove(i)
      
print(lst1)
