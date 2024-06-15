List = eval(input())
List1=List.copy()
for i in List:
    if List1.count(i)>1:
        List1.remove(i)
    elif List1.count(i) == 1:
        continue
print(List1)
