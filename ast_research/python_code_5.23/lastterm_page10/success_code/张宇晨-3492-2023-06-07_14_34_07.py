Str=input()
List=[]
for x in Str:
    a=Str.count(x)
    if a==1:
        List.append(x)
if len(List)==0:
    print("None")
else:
    print(List[0])
