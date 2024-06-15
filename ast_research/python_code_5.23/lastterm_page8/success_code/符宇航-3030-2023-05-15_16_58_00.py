name = input().split(',')
score = input().split(',')
lst = list(zip(name,map(int,score)))
lst1=sorted(lst,key=lambda x:x[1])
lst2=[]
for x in lst1:
    x=list(x)
    lst2.append(x)

print(lst2)
