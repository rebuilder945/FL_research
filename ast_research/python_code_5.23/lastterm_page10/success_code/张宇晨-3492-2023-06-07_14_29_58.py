Str=input()
List=[]
for x in Str:
    a=Str.count(x)
    if a==1:
        List.append(x)
print(List[0])
