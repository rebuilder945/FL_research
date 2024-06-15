List = eval(input())
List1 = List.copy()
for i in List:
    if i == 0:
        List1.remove(0)
    else:
        pass
Nums = len(List)-len(List1)
for x in range(Nums):
    List1.append(0)
print(List1)
