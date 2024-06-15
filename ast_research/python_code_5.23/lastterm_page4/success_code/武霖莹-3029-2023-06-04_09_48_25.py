sName = input().split(',')
sFen = eval(input())
lst = []
for i in range(len(sName)):
    lst.append([sName[i],sFen[i]])
print(lst)

