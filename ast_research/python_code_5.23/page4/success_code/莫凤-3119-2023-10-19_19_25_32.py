list1=eval(input())
for x in list1:
    a=list1.count(x)
    if a>1:
        for y in range(a-1):
            del list1[list1.index(x)]
print(list1)
