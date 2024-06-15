name = input().split(",")
names = list(name)
grades = eval(input())
l = []
for i in range(len(name)):
    ls = [names[i],grades[i]]
    l.append(ls)
print(l)    
    

