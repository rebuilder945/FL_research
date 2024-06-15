a = input().split(" ")
List=[(a[i]) for i in range(len(a))]
List1 = List.copy()
M = input().split(" ")
n,m = M
n = eval(n)
m = eval(m)
if abs(n) > len(List) or abs(m) > len(List):
    pass
else:
    List[ n ] = List1[ m ]
    List[ m ] = List1[ n ]
    print(List)
