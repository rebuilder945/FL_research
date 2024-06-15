Name = input().split(",")
List = [Name[i] for i in range(len(Name))]
Achi = eval(input())
List1 = [[List[x],Achi[x]] for x in range(len(Achi))]
print(List1)

