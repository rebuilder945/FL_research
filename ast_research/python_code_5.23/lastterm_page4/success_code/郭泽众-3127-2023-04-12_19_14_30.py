n = eval(input())
lst =  [x+1 for x in range(n)]
for i in range(1):
    lst.insert(len(lst),lst[0])
    lst.remove(lst[0])
print(lst)
