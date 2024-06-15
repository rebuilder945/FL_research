temp = eval(input())
lst = list(range(1,temp+1))
for i in lst:
    lst.append(i)
    del lst[0]
print(lst)



