lst1 = eval(input())
lst2 = sorted(lst1,reverse = True)
sum = 0
for x in lst2:
    sum = sum * 10 + x
print(sum)
