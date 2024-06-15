temp = eval(input())
lst = list(range(1,temp+1))
for i in range(1):
    lst.append(lst[0])
    del lst(0)
print(lst)



