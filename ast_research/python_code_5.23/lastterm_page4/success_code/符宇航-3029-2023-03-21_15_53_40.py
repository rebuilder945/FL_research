name = input().split(',')
name1 = list(name)
point = eval(input())
duiying = []
for i in range(len(name1)):
    people =(name1[i],point[i])
    duiying.append(list(people))
print(duiying)

