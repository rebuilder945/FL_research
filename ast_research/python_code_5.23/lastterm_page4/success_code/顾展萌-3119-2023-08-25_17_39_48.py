lst = eval(input())
lst1 =[""]
for i in lst:
    if i not in lst1:
        lst1.insert(0,i)
lst1.reverse()
lst1.pop()

print(lst1)

