Name = input().split(",")
Achievement = eval(input())
List1 = []
for i in range(len(Name)):
    A = [Name[i],Achievement[i]]
    List1.append(A)
print(List1)
