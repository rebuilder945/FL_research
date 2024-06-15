n = eval(input())
List = [i for i in range(1,n+1)]
List1 = List.copy()
for x in range(len(List)):
    if x + 1< len(List):
        List[x] = List1[x+1]
    elif x + 1 == len(List):
        List[x] = List1[0] 
print(List)
