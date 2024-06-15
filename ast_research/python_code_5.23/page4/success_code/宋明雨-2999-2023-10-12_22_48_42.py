a = input().split(" ")
List=[(a[i]) for i in range(len(a))]
List1 = List.copy()
n,m = eval(input())
if n > len(List) or m > len(List):
    pass
else:
    List[ n ] = List1[ m ]
    List[ m ] = List1[ n ]
    print(List)
