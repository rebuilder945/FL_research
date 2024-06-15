name=input().split(',')
grades=eval(input())
a=[]
for i in range(len(name)):
    a.append([name[i],grades[i]])
a.sort(key=i[1] for i in a)
print(a)



