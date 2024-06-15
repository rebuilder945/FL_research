names=eval(input())
marks=eval(input())
lst1=list(names)
lst2=list(marks)
result=[]
for x in len(lst1):
    result.append([lst1[x],lst2[x]])
print(result)
