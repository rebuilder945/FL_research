List = eval(input())
List1 = []
for i in List:
    if List.count(i) == 1:
        List1.append(i)
List1.sort()
if List1:
    print(",".join(str(i) for i in List1))
else:
    print("False")
