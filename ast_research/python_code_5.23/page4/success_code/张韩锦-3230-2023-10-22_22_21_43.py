lst=eval(input())
lst2=[]
for i in lst:
    if i == max(lst):
        lst2.append(i*10**len(lst))
        lst.remove(i)
for i in lst:
    if i == max(lst):
        lst2.append(i*10**len(lst))
        lst.remove(i)
for i in lst:
    if i == max(lst):
        lst2.append(i*10**len(lst))
        lst.remove(i)
for i in lst:
    if i == max(lst):
        lst2.append(i*10**len(lst))
        lst.remove(i)
for i in lst:
    if i == max(lst):
        lst2.append(i*10**len(lst))
        lst.remove(i)

            
print(sum(lst2))
