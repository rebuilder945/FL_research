lst = eval(input())
lst1 = ["n"]
for i in lst:
    if i == 0:
        lst1.insert(0,i)
    else:
        lst1.insert(-1,i)
lst1.remove("n")
lst1.reverse()
print(lst1)




