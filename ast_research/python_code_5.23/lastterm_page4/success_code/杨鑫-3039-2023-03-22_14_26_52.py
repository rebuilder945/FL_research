import Max
List=eval(input())
Min=min(List)
while Min in List:
    List.remove(Min)
Max=max(List)
while Max in List:
    List.remove(Max)
print(List)
