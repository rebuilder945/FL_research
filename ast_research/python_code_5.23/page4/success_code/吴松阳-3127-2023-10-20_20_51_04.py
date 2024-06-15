temp = eval(input())
lst = list(range(1,temp+1))
for i in range(1):
    lst.append(lst[0])
    lst.pop(0)
print(lst)



