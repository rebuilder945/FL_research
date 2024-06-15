lst0 = eval(input())
lst0.sort(reverse = True)
lst1 = []
for i in lst0:
    lst1.append(str(i))
num = "".join(lst1)
print(num)
