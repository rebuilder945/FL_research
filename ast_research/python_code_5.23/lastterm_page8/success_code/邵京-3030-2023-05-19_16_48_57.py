name=input().split(',')
grades=eval(input())
a=[]
for i in range(len(name)):
    a.append([name[i],grades[i]])
print(a)

