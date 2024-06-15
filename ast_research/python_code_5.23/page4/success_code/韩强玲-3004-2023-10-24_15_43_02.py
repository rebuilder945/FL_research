lst1 = eval(input())
lst2 = []
for i in lst1:
   if i>=2:
    for x in range(2,i):
      if i%x==0:
        break
    else: 
        lst2.append (i)
print(lst2)
