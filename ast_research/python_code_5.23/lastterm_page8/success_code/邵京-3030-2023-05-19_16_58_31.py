name=input().split(',')
grades=eval(input())
a=[]
for i in range(len(name)):
    a.append([grades[i],name[i]])
a.sort()
for i in a:
    i.reverse()
print(a)



