n = eval(input())
list1 = [n for n in range(1,n+1)]
for i in list1:
    if list1.index(i) == 0:
        list1.remove(i)
        list1.insert(n-1,i)
print(list1)
