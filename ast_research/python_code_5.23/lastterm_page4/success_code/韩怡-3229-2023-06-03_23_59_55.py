List1 = eval(input())
List2 = []
for x in range(len(List1)):
    if List1.count(List1[x]) == 1:
        List2.append(List1[x])
    else:
        pass
List2.sort()
if List2 == []:
    print("False")
else:
    n1 = [str(x) for x in List2]
    n2 = ",".join(n1)
    print(n2)


