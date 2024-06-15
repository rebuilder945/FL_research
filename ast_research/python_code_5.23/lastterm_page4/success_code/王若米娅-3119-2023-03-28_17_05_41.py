lst=eval(input())
lst2=[]
for x in lst[::-1]:
    if x in lst2:
        continue
    else:
        lst2.append(x)
print(lst2[::-1])
